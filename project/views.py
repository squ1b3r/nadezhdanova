from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

import activities.models
import works.models


__all__ = (
    "Frontpage"
)


class Frontpage(TemplateView):

    template_name = "frontpage.html"
    page_title = _(u"Nadya Kutyreva")

    def get_slides(self):
        return works.models.Slide.objects.filter(is_active=True)

    def get_activities(self):
        return activities.models.Activity.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Frontpage, self).get_context_data(**kwargs)
        context["main_slides"] = self.get_slides()
        context["activities"] = self.get_activities()
        return context
