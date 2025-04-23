RDM Get/Set results
###################

To obtain results of RDM GET or SET operations, subscribe to the `rdm_get_set` channel:

.. code-block:: json

  {
      "subscribe": "rdm_get_set"
  }


Updates on this channel will have a `data` object with the following keys:


.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - Key
    - Function
  * - ``"message_type"``
    - string (see below)
  * - ``"universe_id"``
    - The universe ID in Universe Key Format - see below.
  * - ``"device_id"``
    - string in `RDM UID Format`_
  * - ``"pid"``
    - string, RDM PID as a human-readable string, e.g. ``DEVICE_INFO``, or a string containing the hex representation of the enum value of the PID as defined by the RDM standard, e.g. ``c1``
  * - ``"data"``
    - object (optional)

.. include:: ../../snippets/universe-key-string-format-rdm.rst


The `message_types` are:

* ``get_finished``: The GET operation indicated by the PID has finished. No `data` object is expected.
* ``set_finished``: The SET operation indicated by the PID has finished. No `data` object is expected.
* ``result``: Provides the results of the operation, parsed from the response from the device.
* ``result_error``: The operation indicated by the PID has encountered an error parsing the response from the device.
* ``get_cancelled``: The GET operation indicated by the PID has been cancelled.
* ``set_cancelled``: The SET operation indicated by the PID has been cancelled.

For the messages sending data, the `data` object format is described in the following sections.

Get/Set result
**************

``"message_type" : "result"``

The ``data`` object will be appropriate for the PID. If the PID is one of the :doc:`supported PIDs<rdm-supported-pids>`, e.g. ``DEVICE_INFO`` then ``data`` is described under :doc:`rdm-supported-pids`.

For example:

.. code-block:: json

    {
        "broadcast": "rdm_get_set",
        "data": {
            "message_type": "result",
            "universe": "dmx:1",
            "device_id": "7068:3730936e",
            "pid": "DEVICE_MODEL_DESCRIPTION",
            "data": {
                  "model_description": "LDA - Mini RDM Fixture"
            }
        }
    }

Otherwise, ``pid`` will be the hexadecimal representation of the enum value of the PID, and ``data`` will have one key, ``raw``, the value of which will be the base64-encoded raw payload data received from the device.

For example:

.. code-block:: json

   {
      "broadcast": "rdm_get_set",
      "data": {
         "message_type": "result",
         "universe": "dmx:1",
         "device_id": "7068:893b0b82",
         "pid": "8500",
         "data": {
            "raw": "V1MyODEyQg=="
         }
      }
   }

Get/Set result error
********************

``"message_type" : "result_error"``

The ``data`` object will contain:

* ``error``: string, a description of the error with the response


Get/Set operation cancelled
***************************

``"message_type" : "get_cancelled"``

``"message_type" : "set_cancelled"``

The ``data`` object will contain:

* ``error``: string, a description of why the operation was cancelled

For example:

.. code-block:: json

   {
      "broadcast": "rdm_get_set",
      "data": {
         "message_type": "get_cancelled",
         "universe": "dmx:1",
         "device_id": "7068:3730936e",
         "pid": "9999",
         "data": {
            "error": "unknown pid"
         }
      }
   }

RDM UID Format
**************

.. include:: ../../snippets/rdm-uid-format.rst
