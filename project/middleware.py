# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils import translation
from django.utils.cache import patch_vary_headers


class LocaleMiddleware(object):
    """
    Sets current urlconf and language to EN if we have URL startswith with /EN.
    In other cases use default LANGUAGE_CODE for settings.
    """

    LANGUAGE_CODE = "en"

    def get_language(self, request):
        if request.path.startswith("/{0}".format(self.LANGUAGE_CODE)):
            return self.LANGUAGE_CODE
        return settings.LANGUAGE_CODE

    def process_request(self, request):
        language = self.get_language(request)
        translation.activate(language)
        request.LANGUAGE_CODE = language

        if language == self.LANGUAGE_CODE:
            request.urlconf = "project.urls.base_en"
        return None

    def process_response(self, request, response):
        """
        Deactivates locale after request is finished to prevent
        locale liking to the next requests.
        """
        translation.deactivate()
        patch_vary_headers(response, ("Accept-Language",))

        if "Content-Language" not in response:
            response["Content-Language"] = self.get_language(request)
        return response


class AdminLocalMiddleware(object):
    """
    Sets default language for django admin to english no matter what.
    """

    def process_request(self, request):
        if request.path.startswith("/admin"):
            translation.activate(settings.PROJECT_LANGUAGE_CODE)
            request.LANGUAGE_CODE = settings.PROJECT_LANGUAGE_CODE
        return None

    def process_response(self, request, response):
        """
        Deactivates locale after request is finished to prevent
        locale liking to the next requests.
        """
        language = translation.get_language()
        translation.deactivate()

        patch_vary_headers(response, ("Accept-Language",))
        if "Content-Language" not in response:
            response["Content-Language"] = language
        return response
