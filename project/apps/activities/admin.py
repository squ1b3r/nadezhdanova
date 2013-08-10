# -*- coding: utf-8 -*-

from django.contrib import admin

from flatblocks.models import FlatBlock
from imperavi.admin import ImperaviAdmin
from sorl.thumbnail.admin import AdminImageMixin
from suit.admin import SortableTabularInline

from activities.models import Activity, ActivitySlide


class ActivitySlideInline(AdminImageMixin, SortableTabularInline):

    model = ActivitySlide
    extra = 0
    sortable = "order"


class ActivityAdmin(ImperaviAdmin):

    list_display = ("title",)
    inlines = (ActivitySlideInline,)


class FlatBlockAdmin(ImperaviAdmin):

    ordering = ("slug",)
    list_display = ("slug", "header")
    search_fields = ("slug", "header", "content")


admin.site.register(Activity, ActivityAdmin)

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, FlatBlockAdmin)
