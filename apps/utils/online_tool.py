# -*- coding: utf-8 -*-
IMAGE_LIST = [
    "busybox",
    "centos",
    "docker",
    "fedora",
    "golang",
    "httpd",
    "java",
    "jenkins/jenkins",
    "jenkinsci/blueocean",
    "memcached",
    "mongo",
    "mysql",
    "nginx",
    "node",
    "php",
    "postgres",
    "python",
    "rabbitmq",
    "redis",
    "registry",
    "ruby",
    "tomcat",
    "ubuntu",
    "wordpress",
]

IZONE_TOOLS = {
    "office": {
        "tag": "办公工具",
        "tools": [
            {
                "name": "Markdown编辑器",
                "url": "tool:markdown_editor",
                "img": "editor/images/logos/editormd-logo-96x96.png",
                "desc": "基于开源项目 Editor.md 的在线 markdown 编辑器，拥有强大的编辑能力和全面的语法支持",
            }
        ],
    },
    "web": {
        "tag": "站长工具",
        "tools": [
            {
                "name": "百度主动推送工具",
                "url": "tool:baidu_push",
                "img": "blog/img/baidu-2.png",
                "desc": "调用百度站长提供的主动推送接口批量提交链接，提升网站收录效率，老站必备",
            },
            {
                "name": "Sitemap主动推送",
                "url": "tool:baidu_push_site",
                "img": "blog/img/map.png",
                "desc": "抓取Sitemap页面所有链接，调用百度主动推送接口，主动批量提交网站链接，新站必备",
            },
        ],
    },
    "develop": {
        "tag": "开发工具",
        "tools": [
            {
                "name": "Docker镜像查询",
                "url": "tool:docker_search",
                "img": "blog/img/docker.png",
                "desc": "查询官方镜像仓库中指定镜像的版本信息，帮助开发人员更准确的选择合适的镜像",
            },
            {
                "name": "User-Agent生成器",
                "url": "tool:useragent",
                "img": "blog/img/chrome.png",
                "desc": "网页请求头在线生成器，自动生成各种平台和浏览器的请求头User-Agent",
            },
            {
                "name": "HTML特殊字符",
                "url": "tool:html_characters",
                "img": "blog/img/html.png",
                "desc": "HTML常用字符查询表，HTML特殊字符对照表",
            },
            {
                "name": "在线正则表达式",
                "url": "tool:regex",
                "img": "blog/img/regex.png",
                "desc": "正则表达式在线工具，使用正则表达式的规则提取信息，所有语言规则通用",
            },
            {
                "name": "图片转base64",
                "url": "tool:picture_to_base64",
                "img": "blog/img/base64.png",
                "desc": "图片转base64",
            },
            {
                "name": "base64加解密",
                "url": "tool:base64",
                "img": "blog/img/base64-code.jpg",
                "desc": "base64在线加密，解密",
            },
            {
                "name": "颜色转换",
                "url": "tool:color",
                "img": "blog/img/color.jpg",
                "desc": "在线16进制与RGB颜色互转",
            },
        ],
    },
    "query": {
        "tag": "便民工具",
        "tools": [
            {
                "name": "历史上的今天",
                "url": "tool:history_today",
                "img": "blog/img/todayhistory.png",
                "desc": "回顾历史的长河，历史是生活的一面镜子，历史上的今天，看看都发生了什么重大事件",
            },
            {
                "name": "放假安排",
                "url": "tool:holiday",
                "img": "blog/img/holiday.jpeg",
                "desc": "放假安排，看看是不是要放假了",
            },
            {
                "name": "手机号归属地",
                "url": "tool:phone",
                "img": "blog/img/shouji.png",
                "desc": "手机号归属地查询，支持移动，电信，联通",
            }
        ],
    },
}

