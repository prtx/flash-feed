from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    "",
    # Examples:
    # url(r'^$', 'flashfeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^list_category/$", "news.views.servejson"),
    url(r"^fetch/(.*?)/$", "news.views.servejson"),
)
