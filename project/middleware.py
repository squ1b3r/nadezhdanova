from django.conf import settings
from django.utils import translation
from django.utils.cache import patch_vary_headers


__all__ = ("admin_locale_middleware",)


def admin_locale_middleware(get_response):

    def middleware(request):
        if request.path.startswith("/admin"):
            translation.activate(settings.LANGUAGE_CODE)
            request.LANGUAGE_CODE = settings.LANGUAGE_CODE

        response = get_response(request)

        language = translation.get_language()
        translation.deactivate()

        patch_vary_headers(response, ("Accept-Language",))
        if "Content-Language" not in response:
            response["Content-Language"] = language
        return response
    return middleware
