Introduction
############

|Vendor| controllers offer web and Lua APIs providing access to system information, playback functions and trigger operations.

The Lua API is available in trigger action scripts and in IO modules (via the ``controller`` namespace).

In addition, a small JavaScript library is hosted on the controller's web server, which wraps the HTTP requests of the web API and also provides a mechanism to subscribe to the controller's websocket channels via callbacks.
