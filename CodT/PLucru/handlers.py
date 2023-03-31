import os
import shutil

from gi.repository import Gtk

from installdialog import getArchive

class Handlers:
    def onDestroy(self, *args):
        Gtk.main_quit()
    def installWidgetTheme(self, *args):
        filename = getArchive()
        try:
            shutil.unpack_archive(filename, os.path.expanduser(os.path.join("~", ".themes")))
        except:
            pass
    def installIconTheme(self, *args):
        filename = getArchive()
        try:
            shutil.unpack_archive(filename, os.path.expanduser(os.path.join("~", ".icons")))
        except:
            pass