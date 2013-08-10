# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils import translation


class TranslationMeta(models.base.ModelBase):
    """
    Metaclass for using Django Meta options for setting list of fields that
    need to be translated.
    """
    def __new__(self, name, bases, attrs):
        meta = attrs.get("Meta", None)
        translatable_fields = []
        languages = []

        if hasattr(meta, "translatable_fields") and hasattr(meta, "languages"):
            languages = list(meta.languages)
            translatable_fields = list(meta.translatable_fields)

            delattr(meta, "languages")
            delattr(meta, "translatable_fields")

        # Inherits possible translatable_fields and languages from parents.
        abstract_model_bases = [base for base in bases if hasattr(base, "_meta") and base._meta.abstract]
        for base in abstract_model_bases:
            if hasattr(base._meta, "translatable_fields"):
                translatable_fields.extend(list(base._meta.translatable_fields))

            if hasattr(base._meta, "languages"):
                languages.extend(list(base._meta.languages))

        new_class = super(TranslationMeta, self).__new__(self, name, bases, attrs)

        if hasattr(new_class, "_meta"):
            new_class._meta.translatable_fields = tuple(translatable_fields)
            new_class._meta.languages = tuple(languages)
        return new_class


class TranslationMixin(models.Model):
    """
    Model class mixin for getting/setting translatable fields values depending on
    what language is currently active.

        class TranslatableModel(TranslationMixin):

            title = models.CharField()
            title_ru = models.CharField()

            class Meta:
                languages = ("ru",)
                translatable_fields = ("title",)

    How to set:

    >>> from django.utils.translation import activate
    >>> foo.title = "english title"
    >>> activate("ru")
    >>> foo.title = "russian title"
    >>> foo.save()

    How to get:

    >>> foo.title
    u"english title"
    >>> from django.utils.translation import activate
    >>> activate("ru")
    >>> foo.title
    u"russian title"

    """
    __metaclass__ = TranslationMeta

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        """
        Adds `initialized` flag so we could check later that initialization is over
        and we can do our things.

        Used in custom `__setattr__`
        """
        setattr(self, "initialized", False)
        super(TranslationMixin, self).__init__(*args, **kwargs)
        setattr(self, "initialized", True)

    def __getattribute__(self, name):
        """
        Overrides standart `__getattribute__` method in order to `get` values
        depending on current active language.
        """
        language = translation.get_language()

        translatable_fields = object.__getattribute__(self, "_meta").translatable_fields
        languages = object.__getattribute__(self, "_meta").languages

        if language in languages and name in translatable_fields:
            i18n_name = "{0}_{1}".format(name, language)

            if hasattr(self, i18n_name):
                value = object.__getattribute__(self, i18n_name)
                if value:
                    return value
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        """
        Overrides standart `__setattr__` method in order to `set` values
        depending on current active language.
        """
        language = translation.get_language()
        languages = self._meta.languages
        translatable_fields = self._meta.translatable_fields

        if language in languages and name in translatable_fields and getattr(self, "initialized"):
            object.__setattr__(self, "{0}_{1}".format(name, language), value)
        else:
            object.__setattr__(self, name, value)

    def save(self, *args, **kwargs):
        """
        Sets current language to default before `save()` to avoid fields overriding
        and sets it back to what it was before, after `save()`
        """
        language = translation.get_language()
        translation.activate(settings.PROJECT_LANGUAGE_CODE)
        super(TranslationMixin, self).save(*args, **kwargs)
        translation.activate(language)
