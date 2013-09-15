# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

from flatblocks.models import FlatBlock
from sorl.thumbnail.admin import AdminImageMixin
from suit.admin import SortableTabularInline
from redator.widgets import RedactorEditorAdmin

from activities.models import Activity, ActivitySlide


class ActivitySlideInline(AdminImageMixin, SortableTabularInline):

    model = ActivitySlide
    extra = 0
    sortable = "order"


class ActivityAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {"widget": RedactorEditorAdmin}
    }
    list_display = ("title",)
    inlines = (ActivitySlideInline,)


class FlatBlockAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {"widget": RedactorEditorAdmin()}
    }
    ordering = ("slug",)
    list_display = ("slug", "header")
    search_fields = ("slug", "header", "content")


admin.site.register(Activity, ActivityAdmin)

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, FlatBlockAdmin)
