from django.templatetags import i18n
from django.template import Node
from django.urls import reverse
from django.utils import translation

DESCR = """The i18n (internationalisation) tool enables you to override
translations for the Djinn intranet application"""


def get_urls():

    from .urls import urlpatterns

    return urlpatterns


def get_js():

    return []


def get_css():

    return ["djinn_i18n.css"]


def get_info():

    return {"name": "i18n",
            "url": "djinn_i18n_index",
            "description": DESCR,
            "icon": "flag"}


# Monkey patch trans tag
#
original_do_translate = i18n.do_translate


class TranslateNodeWrapper(Node):

    def __init__(self, node, attr=False):

        """ If attr is true-ish, we're within an attribute. If so, don't wrap
        with a span, but set the message id on the element itself. """

        self.node = node
        self.attr = attr

    def render(self, context):

        value = self.node.render(context)

        token = self.node.filter_expression.token.replace('"', '')

        # MJB: Even uitgezet omdat alle vertalingen grijs worden in PG ...
        # if self.attr:
        #     return """%s" data-msgid="%s""" % (value, token)
        # else:
        #     return """<span data-msgid="%s">%s</span>""" % (token, value)

        return """%s""" % (value)


@i18n.register.tag("trans")
def _do_translate(parser, token):

    # TODO: find solution for multiple attrs per element

    attr = False

    close_tag = open_tag = -1
    i = 0

    while close_tag == -1 and open_tag == -1 and i < len(parser.tokens):
        close_tag = parser.tokens[i].contents.find(">")
        open_tag = parser.tokens[i].contents.find("<")
        i += 1

    if close_tag > -1 and (open_tag == -1 or close_tag < open_tag):
        attr = True

    return TranslateNodeWrapper(original_do_translate(parser, token),
                                attr=attr)

#
# MONKEY PATCH translation system
# Als vertaling _EMPTY_ bevat, dan wordt de vertaal-string getoond
#
original_gettext = translation.gettext

def my_gettext(message):

    translated = original_gettext(message)
    if translated in ['_NO_TRANS_', '_NO_TEXT_']:
        return ''

    if translated == '_EMPTY_':
        url = "%s?locale=nl_NL&q=%s" % (reverse('djinn_i18n_search'), message)
        translated = '<b>TO BE TRANSLATED:</b> <a href="%s">"%s"</a>' % (
            url,
            message
        )
    return translated

translation.gettext = my_gettext
translation.gettext_lazy = translation.ugettext_lazy = translation.lazy(my_gettext, str)
