# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from views import Frontpage, SetLanguageView


common_urlpatterns = patterns(None,
    url(r"^$", Frontpage.as_view(), name="frontpage"),
    url(r"^set-language/(?P<language>(?:ru|en))", SetLanguageView.as_view(),
        name="set_language"),
)
