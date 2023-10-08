# CopySite


<pre>
  git clone https://github.com/Muxitdinovich/CopySite.git

  pip install pywebcopy

  cd CopySite
</pre>
Run
<pre>
  python copysite.py
</pre>

<b>Add your site that you want to copy</b>

<pre>
  from pywebcopy import save_webpage, save_website


save_website(

	url = "your website", #Add your site that you want to copy
	project_folder = "C:\ ",
	project_name = "my_site",
	bypass_robots = True,
	debug = True,
	open_in_browser = True,
	delay = None,
	threaded = False,
	
	)
</pre>

🌐 https://hablsearch.netfliy.app
