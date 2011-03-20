from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('radio-locator.locator.views',
    url(r'^get_all_stations/$', "all_stations")
)