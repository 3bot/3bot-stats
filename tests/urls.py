"""URLs to run the tests."""
from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bot/', include('threebot.urls')),
    url(r'^bot-stats/', include('threebot_stats.urls')),
]
