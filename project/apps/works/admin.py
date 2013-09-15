# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.admin import AdminImageMixin
from suit.admin import SortableModelAdmin
from redator.widgets import RedactorEditorAdmin

from works.models import Slide


class SlideAdmin(AdminImageMixin, SortableModelAdmin):

    formfield_overrides = {
        models.TextField: {"widget": RedactorEditorAdmin}
    }
    list_display = ("slide_thumbnail", "title", "is_active")
    list_editable = ("is_active",)
    fields = (
        "image",
        "is_active",
        "title",
        "title_ru",
        "description",
        "description_ru",
        "text",
        "text_ru",
    )
    sortable = "order"

    css = {
        "all": ("/media/css/admin.css",)
    }

    def slide_thumbnail(self, obj):
        if obj.image:
            return u"<img src=\"{0}\" />".format(
                get_thumbnail(obj.image, "250").url
            )
        return ""

    slide_thumbnail.short_description = "Slide"
    slide_thumbnail.allow_tags = True


admin.site.register(Slide, SlideAdmin)
