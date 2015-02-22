\from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, url
from cofy import views

urlpatterns = patterns('',
	url(r'^home/', views.index),
	url(r^joblist/', views.joblists),
	url(r'^job/(?P<event_id>\d+)/(?P<slug>[-\w]+)/', views.job),
)
