from urls import urlpatterns


def get_urls():

    return urlpatterns


def get_js():

    return []  # "djinn_i18n.js"]


def get_css():

    return []  # "djinn_i18n.css"]


def get_info():

    return {"name": "i18n",
            "url": "djinn_i18n_index",
            "description": "Override translations for Django applications",
            "icon": "flag"}
