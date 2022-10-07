Token
#####

Methods
*******

.. _token-http-post:

POST
====

Accepts form data or JSON to authenticate a user's credentials, returning a bearer token if successful.

``POST /token``

The payload, whether form data or JSON, should have the following attributes:

.. include:: snippets/authentication-attributes.rst

If the credentials are valid, the response will have a 200 status code and the payload will be a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``access_token``
     - string
     - The access token to use in subsequent requests to authorise them.
   * - ``expires_in``
     - integer
     - The length of time in seconds before the token expires. Normally ``300``.
   * - ``token_type``
     - string
     - Type of the token. Normally ``"Bearer"``.

To use the token in a request, set the ``Authorization`` header value to ``Bearer {your access token}``, where ``{your access token}`` should be replaced with the value of ``access_token`` in the response.

The response will be a 401 error if the user cannot be authenticated because the username or password are incorrect.

The response will be a 400 error if either attribute is missing or a value is of an invalid type. 
