from django.contrib import messages
from djinn_core.views.admin import AdminMixin
from .index import IndexView

class ReloadView(IndexView, AdminMixin):


    def get(self, request, *args, **kwargs):
        from django.utils.translation import trans_real
        try:
            from threading import local
        except ImportError:
            from django.utils._threading_local import local

        import gettext

        try:
            # Reset gettext.GNUTranslation cache.
            gettext._translations = {}

            # Reset Django by-language translation cache.
            trans_real._translations = {}

            # Delete Django current language translation cache.
            trans_real._default = None

            messages.add_message(request, messages.SUCCESS, "Translations reloaded")

            # this was added in django 1.7 or 1.8. Much better than the
            # previous threadlocal approach
            trans_real.reset_cache(setting='LANGUAGES')

        except AttributeError as e:
            pass

        return super(ReloadView, self).get(request, *args, **kwargs)
