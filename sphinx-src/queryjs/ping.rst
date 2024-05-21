Ping
####

Functions
*********

send_ping
=========

Send a single ping to a remote target.

Reply is broadcast on WebSocket. (see :ref:`websocket_subscribe_ping`)

``send_ping(params, callback)``

``params`` is expected to be an object with the same attributes as the HTTP :ref:`ping-http-post` request.
