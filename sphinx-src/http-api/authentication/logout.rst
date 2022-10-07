Logout
######

Methods
*******

.. _logout-http-get:

GET
===

Ends the user's current session.

``GET /logout``

The request must be authenticated either with a cookie or by sending a valid Bearer token in the ``Authorization`` header.

If the request is made from a web browser using cookie authentication then the cookie will be deleted from the browser by the response. The web browser will reload the page from which the request was made if the ``Referer`` header is set.
