from django.conf.urls import url
from blog.views import *    # 이렇게 수정하면 아래와 같이 views.~ 형식에서 views. 부분을 빼야 함
                              # bookmark.urls에서는 from . import views로 했으므로 views.~ 형식으로 사용해야 함
                              # * 표시는 모든 멤버를 일괄 지정함
urlpatterns = [

      # Example: /
      url(r'^$',      PostLV.as_view(), name='index'),
      # Example: /post/ (same as /)
      url(r'^post/$', PostLV.as_view(), name='post_list'),

      # Example: /post/django-example/
      url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

      # Example: /archive/
      url(r'^archive/$', PostAV.as_view(), name='post_archive'),

      # Example: /2012/
      url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

      # Example: /2012/nov/
      url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

      # Example: /2012/nov/10/
      url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

      # Example: /today/
      url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
]