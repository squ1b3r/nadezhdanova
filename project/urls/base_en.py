# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from project.urls.common import common_urlpatterns


urlpatterns = patterns("",
    url(r"^en/", include(common_urlpatterns)),
)
