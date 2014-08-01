from django.template import Library
from djinn_i18n.tool import TOOL


register = Library()


@register.filter(name="is_override")
def is_override(msgid, locale):

    return TOOL.is_override(msgid, locale)
