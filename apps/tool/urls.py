# -*- coding: utf-8 -*-
from django.urls import path
from .views import (
    Toolview,
    BD_pushview,
    BD_pushview_site,
    regexview,
    useragent_view,
    html_characters,
    docker_search_view,
    editor_view,
    history_today_view, picture_to_base64_view, base64_view,
)

urlpatterns = [
    path("", Toolview, name="total"),  # 工具汇总页
    path("baidu-linksubmit/", BD_pushview, name="baidu_push"),  # 百度主动推送
    path(
        "baidu-linksubmit-sitemap/", BD_pushview_site, name="baidu_push_site"
    ),  # 百度主动推送sitemap
    path("regex/", regexview, name="regex"),  # 正则表达式在线
    path("user-agent/", useragent_view, name="useragent"),  # user-agent生成器
    path(
        "html-special-characters/", html_characters, name="html_characters"
    ),  # HTML特殊字符查询
    path("docker-search/", docker_search_view, name="docker_search"),  # docker镜像查询
    path("markdown-editor/", editor_view, name="markdown_editor"),  # editor.md 工具
    path("history-today/", history_today_view, name="history_today"),  # 历史上的今天
    path("picture-to-base64/", picture_to_base64_view, name="picture_to_base64"),  # 图片转base64
    path("base64/", base64_view, name="base64"),  # base64加解密
]
