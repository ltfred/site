import base64
import datetime

import hutils
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.html import mark_safe
from django.core.cache import cache

from utils.common import hex_to_rgb, rgb_to_hex, generate_response
from .apis.bd_push import push_urls, get_urls
from .apis.holiday import Holiday
from .apis.jisu import JiSu
from .apis.useragent import get_user_agent
from .apis.docker_search import DockerSearch
from .templatetags.tool_tags import get_toollist_by_key


import re
import markdown

from utils.online_tool import IMAGE_LIST


def tool_view(request):
    category = request.GET.get("category", None)
    tools = get_toollist_by_key(category)
    return render(request, "tool/tool.html", context={"tool_list": tools, "category": category})


# 百度主动推送
def bd_push_view(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        url = data.get("url")
        urls = data.get("url_list")
        info = push_urls(url, urls)
        return JsonResponse({"msg": info})
    return render(request, "tool/bd_push.html")


# 百度主动推送升级版，提取sitemap链接推送
def bd_push_site_view(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        url = data.get("url")
        map_url = data.get("map_url")
        urls = get_urls(map_url)
        if urls == "miss":
            info = "{'error':404,'message':'sitemap地址请求超时，请检查链接地址！'}"
        elif urls == "":
            info = "{'error':400,'message':'sitemap页面没有提取到有效链接，sitemap格式不规范。'}"
        else:
            info = push_urls(url, urls)
        return JsonResponse({"msg": info})
    return render(request, "tool/bd_push_site.html")


# 在线正则表达式
def regex_view(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        texts = data.get("texts")
        regex = data.get("r")
        key = data.get("key")
        try:
            lis = re.findall(r"{}".format(regex), texts)
        except:
            lis = []
        num = len(lis)
        if key == "url" and num:
            script_tag = """<script>$(".re-result p").children("a").attr({target:"_blank",rel:"noopener noreferrer"});</script>"""
            result = "<br>".join(["[{}]({})".format(i, i) for i in lis])
        else:
            script_tag = ""
            info = "\n".join(lis)
            result = "匹配到&nbsp;{}&nbsp;个结果：\n".format(num) + "```\n" + info + "\n```"
        result = markdown.markdown(
            result,
            extensions=[
                "markdown.extensions.extra",
                "markdown.extensions.codehilite",
            ],
        )
        return JsonResponse({"result": mark_safe(result + script_tag), "num": num})
    return render(request, "tool/regex.html")


# 生成请求头
def useragent_view(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        d_lis = data.get("d_lis")
        os_lis = data.get("os_lis")
        n_lis = data.get("n_lis")
        d = d_lis.split(",") if len(d_lis) > 0 else None
        os = os_lis.split(",") if len(os_lis) > 0 else None
        n = n_lis.split(",") if len(n_lis) > 0 else None
        result = get_user_agent(os=os, navigator=n, device_type=d)
        return JsonResponse({"result": result})
    return render(request, "tool/useragent.html")


# HTML特殊字符对照表
def html_characters(request):
    return render(request, "tool/characters.html")


# docker镜像查询
def docker_search_view(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        name = data.get("name")
        # 只有名称在常用镜像列表中的搜索才使用缓存，可以避免对名称的过滤
        if name in IMAGE_LIST:
            cache_key = "tool_docker_search_" + name
            cache_value = cache.get(cache_key)
            if cache_value:
                res = cache_value
            else:
                ds = DockerSearch(name)
                res = ds.main()
                total = res.get("total")
                if total and total >= 20:
                    # 将查询到超过20条镜像信息的资源缓存一天
                    cache.set(cache_key, res, 60 * 60 * 24)
        else:
            ds = DockerSearch(name)
            res = ds.main()
        return JsonResponse(res, status=res["status"])
    return render(request, "tool/docker_search.html")


def editor_view(request):
    return render(request, "tool/editor.html")


def history_today_view(request):
    """历史上的今天"""
    code, data = JiSu().get_history_data()
    context = {"history": data}
    return render(request, "tool/history_today.html", context=context)


def picture_to_base64_view(request):
    """图片转base64"""
    if request.is_ajax() and request.method == "POST":
        picture = request.FILES.get("picture", None)
        hutils.check_error(not picture, "请传入图片")
        is_header = request.POST.get("is_header", "true")
        image_base64 = base64.b64encode(picture.read()).decode()
        if is_header == "true":
            type_name = picture.name.split(".")
            return JsonResponse({"result": f"data:image/{type_name[-1]};base64,{image_base64}"})
        return JsonResponse({"result": image_base64})
    return render(request, "tool/picture_to_base64.html")


def base64_view(request):
    """base64加解密"""
    if request.is_ajax() and request.method == "POST":
        texts = request.POST.get("texts", None)
        flag = request.POST.get("flag", None)
        hutils.check_error((not texts or not flag), "请输入内容或操作")
        data = ""
        try:
            if flag == "encode":
                data = base64.b64encode(texts.encode()).decode()
            if flag == "decode":
                data = base64.b64decode(texts).decode()
        except:
            return JsonResponse({"result": "输入的明文或密文有误", "status": 400})
        return JsonResponse({"result": data, "status": 200})
    return render(request, "tool/base64.html")


def holiday_view(request):
    """节假日"""
    year = datetime.date.today().year
    date, code = Holiday().get_legal_holiday(str(year))
    holiday = date["message"]
    return render(request, "tool/holiday.html", {"year": year, "holiday": holiday})


def phone_view(request):
    """手机号归属地"""
    if request.is_ajax() and request.method == "POST":
        phone = request.POST.get("phone", "")
        if not phone:
            return generate_response("", "请输入手机号", -1)
        if not re.match(r"^1[3456789]\d{9}$", phone):
            return generate_response("", "输入的手机号有误", -1)
        data = JiSu().get_phone(phone)
        return generate_response(data["result"], data["msg"], data["status"])
    return render(request, "tool/phone.html")


def color_view(request):
    """RGB与16进制互转"""
    if request.is_ajax() and request.method == "POST":
        color: str = request.POST.get("rgb", "")
        if not color:
            return generate_response("", "请传入要转换的颜色", -1)
        if color.startswith("#"):
            try:
                rgb_color = hex_to_rgb(color)
            except:
                return generate_response("", "错误的16进制颜色", -1)
            return generate_response(
                f"<div>RGB：({rgb_color})</div>",
                "ok",
                0,
                extra=f'色块：<div style="background-color: {color}; width: 50px; height: 30px; display: inline-block;"></div>'
            )
        try:
            hex_color = rgb_to_hex(color)
        except:
            return generate_response("", "错误的RGB颜色", -1)
        return generate_response(
            f"<div>16进制：{hex_color}</div>",
            "ok",
            0,
            extra=f'色块：<div style="background-color: {hex_color}; width: 50px; height: 30px; display: inline-block;"></div>'
        )
    return render(request, "tool/rgb.html")