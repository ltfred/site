# -*- coding: utf-8 -*-
from django.urls import path, re_path
from .views import (
    tool_view,
    bd_push_view,
    bd_push_site_view,
    regex_view,
    useragent_view,
    html_characters,
    docker_search_view,
    editor_view,
    history_today_view,
    picture_to_base64_view,
    base64_view,
    holiday_view,
    phone_view,
    color_view
)

urlpatterns = [
    path("", tool_view, name="total"),  # 工具汇总页
    path("baidu-linksubmit/", bd_push_view, name="baidu_push"),  # 百度主动推送
    path(
        "baidu-linksubmit-sitemap/", bd_push_site_view, name="baidu_push_site"
    ),  # 百度主动推送sitemap
    path("regex/", regex_view, name="regex"),  # 正则表达式在线
    path("user-agent/", useragent_view, name="useragent"),  # user-agent生成器
    path(
        "html-special-characters/", html_characters, name="html_characters"
    ),  # HTML特殊字符查询
    path("docker-search/", docker_search_view, name="docker_search"),  # docker镜像查询
    path("markdown-editor/", editor_view, name="markdown_editor"),  # editor.md 工具
    path("history-today/", history_today_view, name="history_today"),  # 历史上的今天
    path("picture-to-base64/", picture_to_base64_view, name="picture_to_base64"),  # 图片转base64
    path("base64/", base64_view, name="base64"),  # base64加解密
    path("holiday/", holiday_view, name="holiday"),  # 节假日安排
    path("phone/", phone_view, name="phone"),  # 手机号归属地
    path("color/", color_view, name="color"),  # 手机号归属地
]
