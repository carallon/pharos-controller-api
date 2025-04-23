Scene
#####

The Scene subscription allows you to subscribe to changes of active scene.


Subscribe Message
-----------------

.. code-block:: json

   {
      "subscribe": "scene"
   }


Change Message
--------------

When the state of any scene changes, a message is sent out with the following parameters in the ``data`` part of the JSON object:

.. include:: ../snippets/json-attributes-scene.rst

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
