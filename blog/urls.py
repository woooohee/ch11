"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from blog.views import *

urlpatterns = [

    # Example: /
    url(r'^$', PostLV.as_view(), name='index'),

    # Example: /post/ (same as /)
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # Example: /2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # # Example: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    # # Example: /2012/11/
    # url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostMAV.as_view(), name='post_month_archive'),

    # # Example: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
    # # Example: /2012/11/10/
    # url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

    # /blog/tag/ URL 요청을 처리할 뷰 클래스 지정, 태그 클라우드 출력용 뷰
      # Example: /tag/
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),

      # /blog/tag/태그 이름/ 요청을 처리할 뷰 클래스 지정
      # r'...': 이스케이프되지 않는 raw 스트링임을 표시
      # [^/]+ : / 이외 문자가 한번 이상 반복
      # (?u)  : 앞의 표현식을 유니코드로 인식하라고 지정(주소창에 한글 입력 가능하도록)
      # Example: /tag/tagname
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),

    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),

    # Example: /search/  # ch09 1/1
    url(r'^search/$', SearchFormView.as_view(), name='search'),
]


# [^/]+ - 슬래시 아닌글자가 여러개 나오면 이라는 뜻
# (?u) - 앞의 내용을 utf 방식으로 처리해라(한글)