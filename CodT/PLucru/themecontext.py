import os
from configparser import ConfigParser

from gi.repository import GLib

class ThemeContext:
    def __init__(self):
        self.gtk3config = ConfigParser()
        self.gtk2config = ConfigParser()

        self.gtk3config.read(os.path.join(GLib.get_user_config_dir(), "gtk-3.0", "settings.ini"))
        print(self.gtk3config['Settings']['gtk-theme-name'])
