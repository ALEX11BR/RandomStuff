from gi.repository import Gtk

def getArchive():
    dialog = Gtk.FileChooserDialog(
        action=Gtk.FileChooserAction.OPEN
    )
    dialog.add_buttons(
        Gtk.STOCK_CANCEL,
        Gtk.ResponseType.CANCEL,
        Gtk.STOCK_OPEN,
        Gtk.ResponseType.OK,
    )

    builder = Gtk.Builder()
    builder.add_from_file("archivefilefilter.ui")
    filter = builder.get_object("ArchiveFileFilter")
    filter.set_name("Supported archive files")
    dialog.add_filter(filter)

    response = dialog.run()
    filename = dialog.get_filename()
    dialog.destroy()
    return filename