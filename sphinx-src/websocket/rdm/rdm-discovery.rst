RDM Discovery
#############

You can subscribe to updates for RDM discovery by subscribing to the ``rdm_discovery`` channel.

.. code-block:: json

   {
      "subscribe": "rdm_discovery"
   }

Updates on this subscription are sent in the format:


.. code-block:: json

   {
      "broadcast": "rdm_discovery",
      "data": {
         "message_type": "device_found",
         "universe": "dmx:1",
         "data": {}
      }
   }

* Below are the possible message types.
* Universe is the universe ID the operation being reported was performed on.
* The data object contains details on the operation result, described below.

Device found
************

``"message_type" : "device_found"``

The ``data`` object will contain:

* ``"device_info"``: object (see below)
* ``"fixture_num"``: user number of the fixture in the project with the same DMX address and footprint as the discovered device, or `null` if there is no matching fixture in the project.

The ``device_info`` object has keys as described in :doc:`../../http-api/objects/rdm-device-info`.

Example response:

.. code-block:: json

   {
      "broadcast": "rdm_discovery",
      "data": {
         "message_type": "device_found",
         "universe": "dmx:1",
         "data": {
            "device_info": {
               "uid": "7068:3730936e",
               "rdm_protocol_version": 256,
               "device_model_id": 115,
               "product_category": 257,
               "software_version_id": 1693580809,
               "dmx512_footprint": 126,
               "dmx512_personality": 258,
               "dmx512_start_address": 1,
               "sub_device_count": 0,
               "sensor_count": 1
            },
            "fixture_num": null
         }
      }
   }

Discovery Finished
******************

``"message_type" : "finished"``

This message indicates that the discovery process has finished.

The ``data`` object will not be present.

.. code-block:: json

   {
      "broadcast": "rdm_discovery",
      "data": {
         "message_type": "finished",
         "universe": "dmx:1"
      }
   }

Discovery Cancelled
*******************

``"message_type" : "cancelled"``

The ``data`` object will contain:

* ``"error"``: string, a description of why the discovery was cancelled

.. code-block:: json

   {
      "broadcast": "rdm_discovery",
      "data": {
         "message_type": "cancelled",
         "universe": "dmx:1",
         "data": {
            "error": "Operation cancelled by user"
         }
      }
   }
