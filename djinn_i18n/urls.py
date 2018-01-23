from django.conf.urls import include, url
from .views.index import IndexView, SaveView, SearchView
from .views.module import ModuleView
from .views.trans import TransView
from .views.po import POView
from .views.reload import ReloadView
from djinn_auth.decorators import superuser_required


_urlpatterns = [

    url(r"^$",
        superuser_required(IndexView.as_view()),
        name="djinn_i18n_index"),

    url(r"^save$",
        superuser_required(SaveView.as_view()),
        name="djinn_i18n_save"),

    url(r"^reload$",
        superuser_required(ReloadView.as_view()),
        name="djinn_i18n_reload"),

    url(r"^trans/(?P<locale>[a-z]{2}(_[A-Z]{2})?)?/?$",
        superuser_required(TransView.as_view()),
        name="djinn_i18n_trans"),

    url(r"^search$",
        superuser_required(SearchView.as_view()),
        name="djinn_i18n_search"),

    url(r"^po/(?P<locale>[a-z]{2}(_[A-Z]{2})?)/$",
        superuser_required(POView.as_view()),
        name="djinn_i18n_po"),

    url(r"^(?P<module>[\w-]*)/(?P<locale>[\w-]*)/$",
        superuser_required(ModuleView.as_view()),
        name="djinn_i18n_module"),
]


urlpatterns = [
    url(r'^djinn/i18n/', include(_urlpatterns)),
]
