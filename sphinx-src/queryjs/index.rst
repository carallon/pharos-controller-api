JavaScript Query Library
########################

|Vendor| controllers provide a JavaScript library, accessible at ``/default/js/query.js``. Controller projects may have a custom web interface, whose source files may include this library to provide convenient access to the controller HTTP API through JavaScript callbacks and to real time status updates through :doc:`websocket subscriptions <websocket/subscriptions>`.

Including the Library
*********************

The query.js library may be included within the ``<head>`` in any HTML file within a custom web interface created for a |Vendor| |Designer| project as follows:

.. code-block:: html

   <!DOCTYPE html>
   <html>
      <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">
         <!--Include query.js library-->
         <script type="text/javascript" src="/default/js/query.js" defer></script>
      </head>
      <body>
      <!-- etc. -->
      </body>
   </html>

Event Handlers
**************

Functions are provided in the library to set event handlers.

* ``set_success_handler(success)`` - function passed as ``success`` will be called when a websocket connection is successfully established with the controller and when a response is received to an HTTP API request.
* ``set_error_handler(error)`` - function passed as ``error`` will be called when a websocket connection cannot be established with the controller and when an error is encountered as part of making an HTTP API request.
* ``set_restart_handler(restart)`` - function passed as ``restart`` will be called when the controller has restarted, at which point any users must authenticate again.
* ``set_redirect_handler(redirect)`` - function passed as ``redirect`` will be called when a request is unauthorized. The function will be passed the url of the default login page as a string, and may choose to return this (the default behaviour) or return the path of a custom login page.

For example:

.. code-block:: js

   Query.set_redirect_handler((suggestion) => {
     console.log("Suggested redirect: " + suggestion)
     return "/custom-login.html"
   })

Querying and Controlling
************************

The functions provided in query.js for querying and controlling the controller and its current project are in the following sections:

.. toctree::
   :maxdepth: 1

   beacon
   channel
   command
   config
   content-targets
   controller
   group
   input
   log
   lua-variable
   output
   override
   ping
   project
   protocol
   rdm-discovery
   rdm-get
   rdm-set
   remote-device
   replication
   scene
   system
   temperature
   text-slots
   time
   timeline
   trigger

Subscriptions
*************

Websocket subscriptions allow data to be pushed to the web client whenever there is a change within the project. The query.js library includes :doc:`functions <websocket/subscriptions>` with callbacks to subscribe to each channel and return any data received.

.. toctree::
   :hidden:

   websocket/subscriptions
