import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from handlers import Handlers
from themecontext import ThemeContext

builder = Gtk.Builder()
builder.add_from_file("ui.glade")
builder.connect_signals(Handlers())

themecontext = ThemeContext()

win = builder.get_object("mainwindow")
win.resize(600, 400)
win.show()

Gtk.main()