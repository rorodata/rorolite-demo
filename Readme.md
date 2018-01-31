# rorolite demo

Sample ML application to demo [rorolite][1].

[1]: https://github.com/rorodata/rorolite

# How to use

Edit the [rorolite.yml](rorolite.yml) and set the `host` and `user`.

Provision the server to install all required software.

	$ rorolite provision

Deploy the application and all the services.

	$ rorolite deploy
	...
	Services are live at:
	  api -- http://rorolite.do.rorodata.net:8080/	

You the firefly client to access the API. See [test.py](test.py) for more details.


	
