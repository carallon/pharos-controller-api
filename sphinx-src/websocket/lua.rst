Lua
###

Subscribing to Lua values allows the WebSocket to receive data sent by the ``push_to_web()`` Lua function from the controller API.

Subscribe Message
-----------------

.. code-block:: json

   {
      "subscribe": "lua"
   }


Change Message
--------------

For example, if a project needs to send a touch slider level to the WebSocket, it might have the following in a trigger Lua script:

.. code-block:: lua

   level = getMySliderLevel() -- user-defined function to get the current slider level
   push_to_web("slider_level", level) -- invoke callbacks on subscribers

And the data from the WebSocket might look like:

.. code-block:: json

   {
      "broadcast": "lua",
      "data": {
         "slider_level": 56
      }
   }
