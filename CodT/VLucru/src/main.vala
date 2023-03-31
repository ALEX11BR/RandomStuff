using Gtk;

int main (string[] args)
{
	Gtk.init (ref args);

	var builder = new Builder ();
	try
	{
		builder.add_from_file ("interface.glade");
	}
	catch (Error e)
	{
		stderr.printf ("Error while loading UI file: %s\n", e.message);
		return 1;
	}

	var window = builder.get_object ("main_window") as Window;
	window.resize (600, 400);
	window.show ();
	window.destroy.connect (() => {
		Gtk.main_quit ();
	});

	var gtk2_row = builder.get_object ("gtk2_theme_setting_row") as ListBoxRow;
	var gtk2_switch = builder.get_object ("gtk2_different_theme_setting_switch") as Switch;
	// When our "Set a different GTK2 Theme" ModelButton is clicked, let's change its check status
	// (the 'active' property) and make the "GTK2 Theme" option available (i.e. make it visible).
	gtk2_switch.state_set.connect ((state) => {
		gtk2_switch.set_state (state);
		gtk2_row.set_visible (state);
		return true;
	});

	Gtk.main ();
	return 0;

