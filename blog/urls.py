from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.main, name='main'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^activities/(?P<pk1>[0-9]+)/$', views.activities, name='activities'),
	url(r'^sets/(?P<pk3>[0-7])-\d/$', views.gen_sets, name='gen_sets'),
	url(r'^sets/(?P<pk>[0-9]+)/$', views.sets, name = 'sets'),
	url(r'^sets/new/$', views.sets_new, name='sets_new'),
]
