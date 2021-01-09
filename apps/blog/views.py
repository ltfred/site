import datetime
import time

import hutils
import markdown
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from django.views import View, generic
from haystack.generic_views import SearchView  # 导入搜索视图
from haystack.query import SearchQuerySet
from markdown.extensions.toc import TocExtension  # 锚点的拓展

from izone.settings import DEFAULT_FROM_EMAIL, TO_EMAIL

from .models import AboutBlog, Article, Category, Silian, Tag, Timeline
from .tasks import sync_send_mail
from .utils import site_full_url


class ArchiveView(generic.ListView):
    model = Article
    template_name = "blog/archive.html"
    context_object_name = "articles"
    paginate_by = 200
    paginate_orphans = 50


class IndexView(generic.ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"
    paginate_by = getattr(settings, "BASE_PAGE_BY", None)
    paginate_orphans = getattr(settings, "BASE_ORPHANS", 0)

    def get_ordering(self):
        sort = self.kwargs.get("sort")
        if sort == "v":
            return ("-views", "-update_date", "-id")
        return ("-is_top", "-create_date")


class DetailView(generic.DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"

    def get_object(self):
        obj = super(DetailView, self).get_object()
        # 设置浏览量增加时间判断,同一篇文章两次浏览超过半小时才重新统计阅览量,作者浏览忽略
        u = self.request.user
        ses = self.request.session
        the_key = "is_read_{}".format(obj.id)
        is_read_time = ses.get(the_key)
        if u != obj.author:
            if not is_read_time:
                obj.update_views()
                ses[the_key] = time.time()
            else:
                now_time = time.time()
                t = now_time - is_read_time
                if t > 60 * 30:
                    obj.update_views()
                    ses[the_key] = time.time()
        # 获取文章更新的时间，判断是否从缓存中取文章的markdown,可以避免每次都转换
        ud = obj.update_date.strftime("%Y%m%d%H%M%S")
        md_key = "{}_md_{}".format(obj.id, ud)
        cache_md = cache.get(md_key)
        if cache_md:
            obj.body, obj.toc = cache_md
        else:
            md = markdown.Markdown(
                extensions=[
                    "markdown.extensions.extra",
                    "markdown.extensions.codehilite",
                    TocExtension(slugify=slugify),
                ]
            )
            obj.body = md.convert(obj.body)
            obj.toc = md.toc
            cache.set(md_key, (obj.body, obj.toc), 60 * 60 * 12)
        return obj

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data["is_show_danger"] = (datetime.datetime.now() - self.get_object().update_date).days >= 365
        return data


class CategoryView(generic.ListView):
    model = Article
    template_name = "blog/category.html"
    context_object_name = "articles"
    paginate_by = getattr(settings, "BASE_PAGE_BY", None)
    paginate_orphans = getattr(settings, "BASE_ORPHANS", 0)

    def get_ordering(self):
        ordering = super(CategoryView, self).get_ordering()
        sort = self.kwargs.get("sort")
        if sort == "v":
            return ("-views", "-update_date", "-id")
        return ordering

    def get_queryset(self, **kwargs):
        queryset = super(CategoryView, self).get_queryset()
        cate = get_object_or_404(Category, slug=self.kwargs.get("slug"))
        return queryset.filter(category=cate)

    def get_context_data(self, **kwargs):
        context_data = super(CategoryView, self).get_context_data()
        cate = get_object_or_404(Category, slug=self.kwargs.get("slug"))
        context_data["search_tag"] = "文章分类"
        context_data["search_instance"] = cate
        return context_data


class TagView(generic.ListView):
    model = Article
    template_name = "blog/tag.html"
    context_object_name = "articles"
    paginate_by = getattr(settings, "BASE_PAGE_BY", None)
    paginate_orphans = getattr(settings, "BASE_ORPHANS", 0)

    def get_ordering(self):
        ordering = super(TagView, self).get_ordering()
        sort = self.kwargs.get("sort")
        if sort == "v":
            return ("-views", "-update_date", "-id")
        return ordering

    def get_queryset(self, **kwargs):
        queryset = super(TagView, self).get_queryset()
        tag = get_object_or_404(Tag, slug=self.kwargs.get("slug"))
        return queryset.filter(tags=tag)

    def get_context_data(self, **kwargs):
        context_data = super(TagView, self).get_context_data()
        tag = get_object_or_404(Tag, slug=self.kwargs.get("slug"))
        context_data["search_tag"] = "文章标签"
        context_data["search_instance"] = tag
        return context_data


def about_view(request):
    obj = AboutBlog.objects.first()
    if obj:
        ud = obj.update_date.strftime("%Y%m%d%H%M%S")
        md_key = "{}_md_{}".format(obj.id, ud)
        cache_md = cache.get(md_key)
        if cache_md:
            body = cache_md
        else:
            body = obj.body_to_markdown()
            cache.set(md_key, body, 3600 * 24 * 15)
    else:
        repo_url = "https://github.com/ltfred"
        body = '<li>作者 Github 地址：<a href="{}">{}</a></li>'.format(repo_url, repo_url)
    return render(request, "blog/about.html", context={"body": body})


class TimelineView(generic.ListView):
    model = Timeline
    template_name = "blog/timeline.html"
    context_object_name = "timeline_list"


class SilianView(generic.ListView):
    model = Silian
    template_name = "blog/silian.xml"
    context_object_name = "badurls"


# 重写搜索视图，可以增加一些额外的参数，且可以重新定义名称
class MySearchView(SearchView):
    context_object_name = "search_list"
    paginate_by = getattr(settings, "BASE_PAGE_BY", None)
    paginate_orphans = getattr(settings, "BASE_ORPHANS", 0)
    queryset = SearchQuerySet().order_by("-views")


def robots(request):
    site_url = site_full_url()
    return render(request, "robots.txt", context={"site_url": site_url}, content_type="text/plain")


class LinkView(View):
    def get(self, request):
        return render(request, "blog/link.html")

    def post(self, request):
        name, address, desc, email = hutils.get_data(request.POST, "name", "address", "desc", "email", optional=True)
        subject = message = "友链申请"
        html_message = f"网站名称：{name}<br>网站地址：{address}<br>网站简介：{desc}<br>邮箱：{email if email else '无'}"
        sync_send_mail.delay(subject, message, DEFAULT_FROM_EMAIL, TO_EMAIL, html_message=html_message)
        return JsonResponse(
            {"message": f"申请成功<br>网站名称：{name}<br>网站地址：{address}<br>网站简介：{desc}<br>邮箱：{email if email else '无'}"}
        )
