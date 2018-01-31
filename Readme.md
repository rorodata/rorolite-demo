# rorolite demo

Machine Learning application remove background from an image. Built to demo [rorolite][1].

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

# Credits

The background removal model was built by [Alon Burg][2] and [Gidi Superber][3]. This app uses the model built by them. You can find more about their work from their [medium post][4] or [github repo][5].

[2]: https://medium.com/@burgalon
[3]: https://medium.com/@gidishperber
[4]: https://towardsdatascience.com/background-removal-with-deep-learning-c4f2104b3157
[5]: https://gitlab.com/fast-science/background-removal-server
