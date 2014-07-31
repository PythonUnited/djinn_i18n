import json
from django.views.generic import TemplateView
from django.conf import settings
from djinn_i18n.tool import TOOL
from djinn_core.views.admin import AdminMixin


class IndexView(TemplateView, AdminMixin):

    template_name = "djinn_i18n/index.html"

    @property
    def default_language(self):

        return settings.LANGUAGE_CODE

    def list_languages(self):

        return settings.LANGUAGES

    def list_modules(self):

        """ List po files modules """

        return TOOL.list_modules().keys()

    @property
    def tainted(self):

        return TOOL.tainted


class SaveView(IndexView):

    def get(self, request, *args, **kwargs):

        TOOL.save()

        return super(SaveView, self).get(request, *args, **kwargs)
