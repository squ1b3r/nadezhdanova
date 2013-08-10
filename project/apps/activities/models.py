# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField

from i18n.models import TranslationMixin


class Activity(TranslationMixin):

    title = models.CharField(verbose_name=_("Title"), max_length=150)
    title_ru = models.CharField(verbose_name=_("Title (ru)"), max_length=150,
                                blank=True, null=True)

    text = models.TextField(verbose_name=_("Text"))
    text_ru = models.TextField(verbose_name=_("Text (ru)"), blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Activities")
        languages = ("ru",)
        translatable_fields = ("title", "text")

    def __unicode__(self):
        return self.title


class ActivitySlide(models.Model):

    activity = models.ForeignKey(Activity, verbose_name=_("Activity"),
                                 related_name="slides")
    image = ImageField(upload_to="upload/activities/slides",
                       verbose_name=_(u"Activity Slide"))
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("order",)

    def __unicode__(self):
        return u"Slide of {0}".format(self.activity.title)
