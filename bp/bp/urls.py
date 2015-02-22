from cofy import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cofy.views.index'),
    url(r'^job/(?P<job_noc>\w+)/', 'cofy.views.job'),
    url(r'^joblist/', 'cofy.views.joblist'),
    url(r'^about/', 'cofy.views.about'),
)
