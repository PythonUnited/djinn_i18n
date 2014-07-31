import polib
from django.conf import settings
from djinn_i18n.po import load_po


class TransTool(object):

    tainted = False

    def __init__(self):

        self.modules = self.list_modules()
        self.overrides = {}
        self.entries = {}
        self.module_entries = {}

        for locale, language in settings.LANGUAGES:

            self.overrides[locale] = load_po(locale)

        for locale, language in settings.LANGUAGES:

            self.entries[locale] = self._fill_entries(locale)

    def translate(self, msgid, msgstr, locale):

        self.tainted = True

        orig_entry = self.entries[msgid]

        self.overrides[locale].update(
            msgid, msgstr,
            comment=orig_entry.comment,
            tcomment=orig_entry.tcomment
        )

        # update tool
        self.entries[locale][msgid].msgstr = msgstr

    def save(self):

        for po in self.overrides.values():

            po.save()

        self.tainted = False

    def list_modules(self):

        """ List all locale modules and return a map of module, path """

        _modules = {}

        for mod in settings.LOCALE_PATHS:

            modname = mod.split("/")[-2]

            _modules[modname] = mod

        return _modules

    def list_entries(self, module, locale):

        return [self.entries[locale][msgid] for msgid in
                self.module_entries[module]]

    def _list_entries(self, module, locale):

        path = self.modules[module]

        pofile_path = "%s/%s/LC_MESSAGES/django.po" % (path, locale)

        try:
            pofile = polib.pofile(pofile_path)
            return [e for e in pofile if not e.obsolete]
        except:
            return []

    def _fill_entries(self, locale):

        _entries = {}

        for entry in self.overrides[locale]:
            _entries[entry.msgid] = entry

        for module in self.modules.keys():

            self.module_entries[module] = []

            for entry in self._list_entries(module, locale):

                self.module_entries[module].append(entry.msgid)

                if not entry.msgid in _entries.keys():
                    _entries[entry.msgid] = entry

        return _entries

    def find_entry(self, msgid, locale):

        return self.entries[locale][msgid]


TOOL = TransTool()
