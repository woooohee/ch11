from django.conf.urls import url
from . import views
urlpatterns = [

url(r'^bookmark/$', views.BookmarkLV.as_view(), name='index'),

url(r'^bookmark/(?P<pk>\d+)/$', views.BookmarkDV.as_view(), name='detail'),

url(r'^bookmark/t_FBV/$', views.tabularBookmark, name='index_t_FBV'),
url(r'^bookmark/t_CBV/$', views.BookmarkLV.as_view(), name='index_t_CBV'),
]
