from pywebcopy import save_webpage, save_website


save_website(

	url = "your website",
	project_folder = "C:\ ",
	project_name = "my_site",
	bypass_robots = True,
	debug = True,
	open_in_browser = True,
	delay = None,
	threaded = False,
	
	)