from django.conf.urls.defaults import patterns, include, url
from views.index import IndexView, SaveView, SearchView
from views.module import ModuleView
from views.trans import TransView


_urlpatterns = patterns(
    "",

    url(r"^$",
        IndexView.as_view(),
        name="djinn_i18n_index"),

    url(r"^save$",
        SaveView.as_view(),
        name="djinn_i18n_save"),

    url(r"^(?P<module>[\w-]*)/(?P<locale>[\w-]*)/$",
        ModuleView.as_view(),
        name="djinn_i18n_module"),

    url(r"^trans/(?P<msgid>.*)/(?P<locale>[a-z]{2}_[A-Z]{2})/$",
        TransView.as_view(),
        name="djinn_i18n_trans"),

    url(r"^search$",
        SearchView.as_view(),
        name="djinn_i18n_search"),
    )


urlpatterns = patterns(
    '',
    (r'^djinn/i18n/', include(_urlpatterns)),
    )
