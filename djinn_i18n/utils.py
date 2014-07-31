from django.conf import settings


def get_override_base():

    return getattr(settings, "PO_OVERRIDES",
                   "%s/var/locale" % settings.PROJECT_ROOT)


def generate_po_path(base, locale):

    return "%s/%s/LC_MESSAGES/django.po" % (base, locale)
