from django.templatetags import i18n
from django.template import Node
from urls import urlpatterns


def get_urls():

    return urlpatterns


def get_js():

    return ["djinn_i18n.js"]


def get_css():

    return ["djinn_i18n.css"]


def get_info():

    return {"name": "i18n",
            "url": "djinn_i18n_index",
            "description": "Override translations for Djinn applications",
            "icon": "flag"}


# Monkey patch trans tag
#
original_do_translate = i18n.do_translate


class TranslateNodeWrapper(Node):

    def __init__(self, node):

        self.node = node

    def render(self, context):

        value = self.node.render(context)

        token = self.node.filter_expression.token.replace('"', '')

        return """<span data-msgid="%s">%s</span>""" % (token, value)


@i18n.register.tag("trans")
def _do_translate(parser, token):

    return TranslateNodeWrapper(original_do_translate(parser, token))
