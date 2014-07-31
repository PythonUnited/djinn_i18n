from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from djinn_core.views.admin import AdminMixin
from djinn_i18n.tool import TOOL


class TransView(TemplateView, AdminMixin):

    template_name = "djinn_i18n/trans.html"

    @property
    def msgid(self):

        return self.kwargs.get('msgid')

    @property
    def locale(self):

        return self.kwargs.get('locale')

    def get(self, request, *args, **kwargs):

        self.entry = TOOL.find_entry(self.msgid, self.locale)

        return super(TransView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        TOOL.translate(self.msgid, request.POST.get('msgstr'), self.locale)

        return HttpResponseRedirect(reverse("djinn_i18n_index"))
