# -*- coding: utf-8 -*-
IMAGE_LIST = ['busybox', 'centos', 'docker', 'fedora', 'golang', 'httpd',
              'java', 'jenkins/jenkins', 'jenkinsci/blueocean', 'memcached',
              'mongo', 'mysql', 'nginx', 'node', 'php', 'postgres', 'python',
              'rabbitmq', 'redis', 'registry', 'ruby', 'tomcat', 'ubuntu', 'wordpress']

IZONE_TOOLS = {
    'office': {
        'tag': '办公工具',
        'tools': [
            {
                'name': 'Markdown编辑器',
                'url': 'tool:markdown_editor',
                'img': 'editor/images/logos/editormd-logo-96x96.png',
                'desc': '基于开源项目 Editor.md 的在线 markdown 编辑器，拥有强大的编辑能力和全面的语法支持'
            }
        ]
    },
    'web': {
        'tag': '站长工具',
        'tools': [
            {
                'name': '百度主动推送工具',
                'url': 'tool:baidu_push',
                'img': 'blog/img/baidu-2.png',
                'desc': '调用百度站长提供的主动推送接口批量提交链接，提升网站收录效率，老站必备'
            },
            {
                'name': 'Sitemap主动推送',
                'url': 'tool:baidu_push_site',
                'img': 'blog/img/map.png',
                'desc': '抓取Sitemap页面所有链接，调用百度主动推送接口，主动批量提交网站链接，新站必备'
            }
        ]
    },
    'develop': {
        'tag': '开发工具',
        'tools': [
            {
                'name': 'Docker镜像查询',
                'url': 'tool:docker_search',
                'img': 'blog/img/docker.png',
                'desc': '查询官方镜像仓库中指定镜像的版本信息，帮助开发人员更准确的选择合适的镜像'
            },
            {
                'name': 'User-Agent生成器',
                'url': 'tool:useragent',
                'img': 'blog/img/chrome.png',
                'desc': '网页请求头在线生成器，自动生成各种平台和浏览器的请求头User-Agent'
            },
            {
                'name': 'HTML特殊字符',
                'url': 'tool:html_characters',
                'img': 'blog/img/html.png',
                'desc': 'HTML常用字符查询表，HTML特殊字符对照表'
            },
            {
                'name': '在线正则表达式',
                'url': 'tool:regex',
                'img': 'blog/img/regex.png',
                'desc': '正则表达式在线工具，使用正则表达式的规则提取信息，所有语言规则通用'
            }
        ]
    },
    'query': {
        'tag': '查询工具',
        'tools': [
            {
                'name': '历史上的今天',
                'url': 'tool:history_today',
                'img': 'blog/img/todayhistory.png',
                'desc': '历史上的今天发生了那些事'
            }
        ]
    },
}

if __name__ == '__main__':
    print(sorted(IMAGE_LIST))
