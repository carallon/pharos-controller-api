Remote Device
#############

The Remote Device endpoint allows a list of remote devices to be requested, and can be subscribed to to recieve data on change of online status of remote devices.


Subscribe Message
-----------------

.. code-block:: json

   {
      "subscribe": "remote_device"
   }


Change Message
--------------

.. code-block:: json

    {
      "data": {
         "remote_devices": [
            {
               "name": "EDN 20 1",
               "name_with_type": "EDN 20 1",
               "num": 1,
               "online": false,
               "serial": [],
               "type": "EDN 20"
            }
            ]
      }
    }

The JSON data about the remote devices is the same as returned from the :ref:`Remote Device HTTP API call<remote-device-http-get>`.
