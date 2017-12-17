from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$',serve, {'document_root': settings.MEDIA_ROOT}),
]
