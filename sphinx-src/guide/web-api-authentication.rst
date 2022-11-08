Web API Authentication
######################

If the controller has security setup then some endpoints of the HTTP API and some functions in the JavaScript library will require clients to authenticate in order to authorise the requests.

Authentication Methods
**********************

Two methods for authenticating users of the Web API are supported:

* `Cookie Authentication`_: the default when using the API and/or query.js library in a custom web interface.
* `Token Authentication`_: used with HTTP API requests, typically when the client is not a web browser.

With both methods, a new token, valid for 5 minutes, is returned from each authenticated request. If the user, or API client, is inactive for longer than 5 minutes then the cookie or token expires, requiring a username and password to be provided again.

Cookie Authentication
=====================

Cookie authentication is typically used by the controller's web interface (either the default web interface or a custom web interface in a project). It works with both the HTTP API and the query.js library.

A cookie is returned by the controller in response to a :ref:`authenticate-http-post` request to the ``/authenticate`` endpoint when the ``original_url`` is provided as a cookie or a query parameter. This is the endpoint used by the default login page whenever a user signs in.

The cookie is stored by a web browser automatically, and the browser then sends this cookie with subsequent requests to authenticate the user. The response from each authenticated request will update this cookie with a new token, valid for 5 minutes. If no authenticated requests are made for 5 minutes then the token in the cookie will expire and the ``/authenticate`` endpoint must be used to get a new token.

The cookie can be removed by making a :ref:`logout-http-get` request to the ``/logout`` endpoint, which can be done simply by navigating the browser to that endpoint.

Custom Login Page
-----------------

Normally, a user will sign into the controller using the login page of the default web interface, which is shown if a user tries to visit a page that they don't have access to. In a custom web interface, uploaded as part of a project, a custom login page can be configured with the ``LoginFile`` directive in the ``.webconfig`` file of the custom web interface. This custom login page is then shown instead of the default login page when a user tries to visit part of a custom web interface that they don't have access to.

Typically a login page will be an HTML page with a form element containing fields for the username and password. The HTML snippet below can be used to generate a form with these fields:

.. code-block:: html

   <form action="/authenticate" method="POST">
     <input type="text" name="user">
     <input type="password" name="password">
     <button type="submit">Submit</button>
   </form>

The form's action is set to POST the form to the controller's ``/authenticate`` endpoint. The ``original_url`` cookie will have been set by the webserver automatically, and will be sent by the browser as part of the POST request. If authentication is successful, the response from the controller will contain a ``token`` cookie, which the browser will store automatically.

Token Authentication
====================

Token authentication is typically used by the HTTP API in cases where a web browser is not the client. The client requests a Bearer Token with a :ref:`authenticate-http-post` request to the controller's ``/authenticate`` endpoint, providing the username and password, and this token is then used in future requests.

To use the token in a request, set the ``Authorization`` header value to ``Bearer {your token}``, where ``{your token}`` should be replaced with the value of ``token`` in the response.

The JSON object in the response from each authenticated request will include a ``token`` attribute, whose value will be a new token, valid for 5 minutes. If no authenticated requests are made for 5 minutes then the token will expire and the ``/authenticate`` endpoint must be used to get a new token.
