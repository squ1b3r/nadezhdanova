import django.db.models
import django.contrib.admin

import sorl.thumbnail.admin

import activities.models


class ActivitySlideInline(sorl.thumbnail.admin.AdminImageMixin, django.contrib.admin.TabularInline):

    model = activities.models.ActivitySlide
    extra = 0
    sortable = "order"


@django.contrib.admin.register(activities.models.Activity)
class ActivityAdmin(django.contrib.admin.ModelAdmin):

    list_display = ("title",)
    inlines = (ActivitySlideInline,)
