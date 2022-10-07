Authorise
#########

Methods
*******

.. _authorise-http-post:

POST
====

Accepts form data or JSON to authenticate a user's credentials, returning a cookie if successful.

``POST /authorise``

The payload, whether form data or JSON, should have the following attributes:

.. include:: snippets/authentication-attributes.rst

If the credentials are valid, a redirect response will be returned, pointing to the value of the ``original_url`` cookie sent with the original request, or ``/`` if this cookie wasn't present.

If the user cannot be authenticated because the username or password are incorrect then a redirect response will be returned, pointing to the value of the ``Referer`` header in the request.

The response will be a 400 error if either attribute is missing or a value is of an invalid type. 
