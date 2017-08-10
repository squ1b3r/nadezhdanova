from django import template
from django.conf import settings
from django.utils import translation
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def trans_field(obj, field):
    language = translation.get_language()
    if language == settings.LANGUAGE_CODE:
        return mark_safe(getattr(obj, field))
    return mark_safe(getattr(obj, "{}_ru".format(field)))
