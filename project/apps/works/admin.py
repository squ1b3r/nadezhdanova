# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import ModelForm

from suit_ckeditor.widgets import CKEditorWidget
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.admin import AdminImageMixin
from suit.admin import SortableModelAdmin

from works.models import Slide

editor_options = {
    "toolbar": [
        ['Source', '-', 'Bold', 'Italic']
    ]
}


class SlideAdminForm(ModelForm):

    class Meta:
        widgets = {
            "description": CKEditorWidget(editor_options=editor_options),
            "description_ru": CKEditorWidget(editor_options=editor_options),
            "text": CKEditorWidget(editor_options=editor_options),
            "text_ru": CKEditorWidget(editor_options=editor_options)
        }


class SlideAdmin(AdminImageMixin, SortableModelAdmin):

    form = SlideAdminForm
    list_display = ("slide_thumbnail", "title", "is_active",)
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
