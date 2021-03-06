from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views


admin.autodiscover()


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^i18n/", include("django.conf.urls.i18n")),

    url(r"^$", views.Frontpage.as_view(), name="frontpage"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
