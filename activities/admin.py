import django.contrib.admin

import sorl.thumbnail.admin

import activities.models


class ActivitySlideInline(sorl.thumbnail.admin.AdminImageMixin, django.contrib.admin.TabularInline):

    model = activities.models.ActivitySlide
    extra = 0
    sortable = "order"


@django.contrib.admin.register(activities.models.Activity)
class ActivityAdmin(django.contrib.admin.ModelAdmin):

    list_display = ("title", "order")
    list_editable = ("order",)
    inlines = (ActivitySlideInline,)
    sortable = "order"

    class Media:
        js = (
            "/static/js/lib/trumbowyg.min.js",
            "/static/js/admin.js"
        )

        css = {
            "all": ("/static/styles/css/lib/trumbowyg.min.css",)
        }
