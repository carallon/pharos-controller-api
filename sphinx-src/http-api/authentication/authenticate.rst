Authenticate
############

Methods
*******

.. _authenticate-http-post:

POST
====

Accepts form data or JSON to authenticate a user's credentials.

``POST /authenticate``

The payload, whether form data or JSON, should have the following attributes:

.. include:: snippets/authentication-attributes.rst

If the credentials are valid, a JSON web token (JWT) is returned. This token is returned either as a ``token`` cookie or in a JSON object with a ``token`` attribute, depending on whether the `original_url`_ parameter was sent with the request.

To use a token returned in a JSON object to authorise a request, set the ``Authorization`` header value to ``Bearer {your token}``, where ``{your token}`` should be replaced with the value of ``token`` in the response from ``/authenticate``.

If the user cannot be authenticated because the username or password are incorrect then a redirect response will be returned, pointing to the value of the ``Referer`` header in the request.

The response will be a 400 error if either attribute is missing or a value is of an invalid type.

original_url
------------

The ``original_url`` parameter is typically used when authenticating the user from form data sent from a web page. Its value is set to the path of the page from where the user was redirected to the login page, and its where the response from ``/authenticate`` will redirect the browser upon successful authentication. It can be sent as a cookie or a query parameter with the ``/authenticate`` request. Its presence in the request will result in the response from ``/authenticate`` setting a cookie with the JWT, rather than returning a JSON object containing the JWT.

For example, if an unauthenticated or unauthorised user attempts to access the configuration page of the built-in web interface, they would try to navigate to ``/default/config.lsp`` but the controller's web server would redirect them to ``default/login.lsp`` and set the ``original_url`` cookie to ``/default/config.lsp``.

In a custom web interface using ``.webconfig`` files to configure access control, the ``original_url`` cookie is automatically set by the web server when redirecting to the login page (which may be a custom login page) when the user attempts to access a restricted page for which they are not authorised.

In both cases, when the login page submits a request to ``/authenticate``, the ``original_url`` cookie will be sent automatically by the browser. A successful response will redirect to the value of ``original_url`` and store a ``token`` cookie in the browser with the user's JWT.
