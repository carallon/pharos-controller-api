Timeline
########

The Timeline subscription allows you to subscribe to changes to active timelines or timeline state.


Subscribe Message
-----------------

.. code-block:: json

   {
      "subscribe": "timeline"
   }


Change Message
--------------

When the state of any scene changes, a message is sent out with the following parameters in the ``data`` part of the JSON object:

.. include:: ../snippets/json-attributes-timeline.rst

For example:

.. code-block:: js

   {
      "broadcast": "scene",
      "data": {
         "num": 1,
         "onstage": true,
         "state": "started"
      }
   }
