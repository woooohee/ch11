
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView

# from bookmark.views import BookmarkLV, BookmarkDV # 이 부분은 bookmark.urls 부분으로 옮겼음

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),

    url(r'^blog/', include('blog.urls', namespace='blog')),

]