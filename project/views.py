# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import redirect
from django.core.urlresolvers import reverse, resolve, NoReverseMatch
from django.views.generic import TemplateView, View
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from pytumblr import TumblrRestClient

from activities.models import Activity
from works.models import Slide


class Frontpage(TemplateView):

    template_name = "frontpage.html"
    page_title = _(u"Nadya Kutyreva")

    def get_main_slides(self):
        return Slide.objects.filter(is_active=True)

    def get_activities(self):
        return Activity.objects.all()

    def get_tumblr_posts(self, amount):
        client = TumblrRestClient(
            settings.TUMBLR_CONSUMER_KEY,
            settings.TUMBLR_CONSUMER_SECRET,
            settings.TUMBLR_OAUTH_TOKEN2,
            settings.TUMBLR_OAUTH_SECRET
        )
        blog_name = "nadezhdanova-eng.tumblr.com"

        language = translation.get_language()
        if language == settings.LANGUAGE_CODE:
            blog_name = "nadezhdanova.tumblr.com"

        response = client.posts(blog_name, type="text", limit=amount, filter="text")
        tumblr_posts = response.get("posts", [])

        posts = []
        for post in tumblr_posts:
            item = {
                "title": post.get("title", ""),
                "text": post.get("body", ""),
                "url": post.get("post_url", "")
            }
            posts.append(item)
        return posts

    def get_context_data(self, **kwargs):
        context = super(Frontpage, self).get_context_data(**kwargs)
        context["main_slides"] = self.get_main_slides()
        context["activities"] = self.get_activities()
        context["tumblr_posts"] = self.get_tumblr_posts(3)
        return context


class SetLanguageView(View):

    def get_default_url(self):
        return reverse("frontpage")

    def get(self, request, *args, **kwargs):
        source_url = request.GET.get("from")
        language = kwargs.get("language")

        if not source_url or (request.path.startswith("/en") and language == "en"):
            return redirect(self.get_default_url())

        url_parts = source_url.split("?")

        if url_parts:
            resolver = resolve(url_parts[0])

            if language == "en":
                urlconf = u"project.urls.base_en"
            else:
                urlconf = u"project.urls.base"

            viewname = resolver.url_name

            if resolver.namespace:
                viewname = "{0}:{1}".format(resolver.namespace, resolver.url_name)

            try:
                new_url = reverse(
                    viewname=viewname,
                    urlconf=urlconf,
                    kwargs=resolver.kwargs
                )
            except NoReverseMatch:
                return redirect(redirect(self.get_default_url()))
            else:
                if len(url_parts) == 2:
                    new_url = new_url + "?" + url_parts[1]
                return redirect(new_url)
        return redirect(redirect(self.get_default_url()))
