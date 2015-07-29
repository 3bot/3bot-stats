"""URLs for the threebot_stats app."""

from django.conf.urls import url

from threebot_stats import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<workflow_id>[0-9]+)/$', views.detail, name='detail'),
]