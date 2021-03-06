import django.db.models
import django.contrib.admin
import django.utils.html

import sorl.thumbnail
import sorl.thumbnail.admin

import works.models


@django.contrib.admin.register(works.models.Slide)
class SlideAdmin(sorl.thumbnail.admin.AdminImageMixin, django.contrib.admin.ModelAdmin):

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

    class Media:
        js = (
            "/static/js/lib/trumbowyg.min.js",
            "/static/js/admin.js"
        )

        css = {
            "all": (
                "/static/styles/css/lib/trumbowyg.min.css",
                "/media/css/admin.css",
            )
        }

    def slide_thumbnail(self, obj):
        if obj.image:
            return django.utils.html.format_html(
                """<img src=\"{0}\" />""",
                sorl.thumbnail.get_thumbnail(obj.image, "250").url
            )
        return ""

    slide_thumbnail.short_description = "Slide"
