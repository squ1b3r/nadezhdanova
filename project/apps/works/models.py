# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField

from i18n.models import TranslationMixin


class Slide(TranslationMixin):

    title = models.CharField(verbose_name=_(u"Title"), max_length=50)
    title_ru = models.CharField(verbose_name=_(u"Title (ru)"), max_length=50,
                                blank=True, null=True)

    description = models.TextField(verbose_name=_(u"Description"))
    description_ru = models.TextField(verbose_name=_(u"Description (ru)"),
                                      blank=True, null=True)

    text = models.TextField(verbose_name=_(u"Text"), blank=True)
    text_ru = models.TextField(verbose_name=_(u"Text (ru)"), blank=True, null=True)

    is_active = models.BooleanField(default=True, verbose_name=_(u"Display"))
    image = ImageField(upload_to="upload/slides", verbose_name=_(u"Slide"))
    order = models.PositiveIntegerField(default=0)

    class Meta:
        languages = ("ru",)
        translatable_fields = ("title", "description", "text")
        ordering = ("order",)

    def __unicode__(self):
        return self.title
