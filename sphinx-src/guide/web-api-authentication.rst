Web API Authentication
######################

If the controller has an admin password or the current project has users configured under Web Interface Access, then some endpoints of the HTTP API and some functions in the JavaScript library will require clients to authenticate in order to authorise the requests.

Authentication Methods
**********************

Two methods for authenticating users of the Web API are supported:

* `Cookie Authentication`_: the default when using the API and/or query.js library in a custom web interface.
* `Token Authentication`_: used with HTTP API requests, typically when the client is not a web browser.

With both methods, if the user is inactive for longer than 5 minutes then the cookie or token expires, requiring a username and password to be provided again.

Cookie Authentication
=====================

Cookie authentication is typically used by the controller's web interface (either the default web interface or a custom web interface in a project). It works with both the HTTP API and the query.js library.

A cookie is returned by the controller in response to a :ref:`authorise-http-post` request to the ``/authorise`` endpoint - this is where the default login page sends the user's username and password when they login. The cookie is stored by a web browser automatically, and the browser then sends this cookie with subsequent requests to authenticate the user. The cookie can be removed by making a :ref:`logout-http-get` request to the ``/logout`` endpoint, which can be done simply by navigating the browser to that endpoint.

Custom Login Page
-----------------

Normally, a user will sign into the controller using the login page of the default web interface, which is shown if a user tries to visit a page that they don't have access to. In a custom web interface, uploaded as part of a project, a custom login page can be configured with the ``AuthFormLoginRequiredLocation`` directive in the main ``.htaccess`` file of the custom web interface. This custom login page is then shown instead of the default login page when a user tries to visit part of a custom web interface that they don't have access to.

Typically a login page will be an HTML page with a form element containing fields for the username and password. The HTML snippet below can be used to generate a form with these fields:

.. code-block:: html

   <form action="/authorise" method="POST">
     <input type="text" name="user">
     <input type="password" name="password">
     <button type="submit">Submit</button>
   </form>

The form's action is set to POST the form to the controller's ``/authorise`` endpoint. If login is successful, the response from the controller will contain a cookie, which the browser will store automatically.

Token Authentication
====================

Token authentication is typically used by the HTTP API in cases where a web browser is not the client. The client requests a Bearer Token with a :ref:`token-http-post` request to the controller's ``/token`` endpoint, providing the username and password, and this token is then used in future requests.
