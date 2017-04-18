from django.conf.urls import include, url
from .views.index import IndexView, SaveView, SearchView
from .views.module import ModuleView
from .views.trans import TransView
from .views.po import POView
from .views.reload import ReloadView


_urlpatterns = [

    url(r"^$",
        IndexView.as_view(),
        name="djinn_i18n_index"),

    url(r"^save$",
        SaveView.as_view(),
        name="djinn_i18n_save"),

    url(r"^reload$",
        ReloadView.as_view(),
        name="djinn_i18n_reload"),

    url(r"^trans/(?P<locale>[a-z]{2}(_[A-Z]{2})?)?/?$",
        TransView.as_view(),
        name="djinn_i18n_trans"),

    url(r"^search$",
        SearchView.as_view(),
        name="djinn_i18n_search"),

    url(r"^po/(?P<locale>[a-z]{2}(_[A-Z]{2})?)/$",
        POView.as_view(),
        name="djinn_i18n_po"),

    url(r"^(?P<module>[\w-]*)/(?P<locale>[\w-]*)/$",
        ModuleView.as_view(),
        name="djinn_i18n_module"),
]


urlpatterns = [
    url(r'^djinn/i18n/', include(_urlpatterns)),
]
