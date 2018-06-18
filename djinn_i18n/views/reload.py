from django.contrib import messages
from djinn_core.views.admin import AdminMixin
from .index import IndexView


class ReloadView(IndexView, AdminMixin):

    def get(self, request, *args, **kwargs):

        from django.utils.translation import trans_real

        try:
            messages.add_message(
                request, messages.SUCCESS, "Translations reloaded")

            # this was added in django 1.7 or 1.8. Much better than the
            # previous threadlocal approach
            trans_real.reset_cache(setting='LANGUAGES')

        except AttributeError as e:
            pass

        return super(ReloadView, self).get(request, *args, **kwargs)
