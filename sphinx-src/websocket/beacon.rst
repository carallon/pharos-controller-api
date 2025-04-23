Beacon
######

The `beacon` channel provides updates on the beacon state of the controller.

The data in the message contains a single boolean value, `on`, which indicates if the Beacon is on or off.

Subscribe Message
-----------------

.. code-block:: json

   {
      "subscribe": "beacon"
   }


Change Message
--------------

.. code-block:: json

   {
      "broadcast": "beacon",
      "data": {
         "on": false
      }
   }
