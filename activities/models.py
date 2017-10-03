from django.db import models
from django.utils.translation import ugettext_lazy as _

import sorl.thumbnail


__all__ = (
    "Activity",
    "ActivitySlide",
)


class Activity(models.Model):

    title = models.CharField(verbose_name=_("Title"), max_length=150)
    title_ru = models.CharField(verbose_name=_("Title (ru)"), max_length=150, blank=True, null=True)

    text = models.TextField(verbose_name=_("Text"))
    text_ru = models.TextField(verbose_name=_("Text (ru)"), blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("-order",)
        verbose_name_plural = _("Activities")

    def __str__(self):
        return self.title


class ActivitySlide(models.Model):

    activity = models.ForeignKey(Activity, verbose_name=_("Activity"), related_name="slides")
    image = sorl.thumbnail.ImageField(upload_to="upload/activities/slides", verbose_name=_(u"Activity Slide"))
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return "Slide for {0}".format(self.activity)
