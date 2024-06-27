RDM Set
#######

Methods
*******

.. _rdm-set-http-post:

POST
====

Request to start an RDM Set operation. A ``202`` response will be returned if the request has been successfully queued. Results are available via a websocket subscription (see :ref:`websocket_subscribe_rdm_get_set`).

``POST /api/rdm/set``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 3 5 3
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``universe``
     - string in `Universe Key String Format`_ or :doc:`objects/rdm-universe-key`
     - The universe on which to perform the RDM Set operation.
     - ``"dmx:2"``
   * - ``destination_uid``
     - string
     - Format is ``{manuId}:{deviceId}(:{subId})``
       where ``{manuId}`` is a padded unsigned hexadecimal integer of width 4, lowercase, e.g. ``072c``;
       ``{deviceId}`` is a padded unsigned hexadecimal integer of width 8, lowercase, e.g. ``0004fe02``;
       ``{subId}`` is an optional unsigned decimal integer.
     - ``"072c:0004fe02"``
   * - ``pid``
     - string
     - RDM PID for the Set operation. Can be one of the `Supported RDM PIDs`_ or the raw PID value as a hex string, e.g. ``"FF"``.
     - ``"DEVICE_INFO"``
   * - ``meta``
     - object
     - Optional. Metadata for the PID, i.e. query params (see `Meta`_).
     -
   * - ``max_rx_length``
     - integer
     - Optional. Expected length of the response data. Only relevant if a raw PID value has been provided for ``pid``. If not provided then the controller must wait for a timeout before handling a response to ensure all response data has been received from the device.
     -

Meta
----

DEVICE_LABEL
^^^^^^^^^^^^

For the ``DEVICE_LABEL`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``label``
     - string
     - Ascii text label for the device. Up to 32 characters.

IDENTIFY_DEVICE
^^^^^^^^^^^^^^^

For the ``IDENTIFY_DEVICE`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``enable``
     - boolean
     - Whether to enable/disable IDENTIFY_DEVICE mode over RDM.

DMX_START_ADDRESS
^^^^^^^^^^^^^^^^^

For the ``DMX_START_ADDRESS`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``start_address``
     - integer
     - DMX start address to set on the device.

DMX_PERSONALITY
^^^^^^^^^^^^^^^

For the ``DMX_PERSONALITY`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``personality``
     - integer
     - Index of the personality to set as current.

SENSOR_VALUE
^^^^^^^^^^^^

For the ``SENSOR_VALUE`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``sensor_number``
     - integer
     - Sensor number to reset.

LAMP_HOURS
^^^^^^^^^^

For the ``LAMP_HOURS`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``lamp_hours``
     - integer
     - Starting value to set on the device's lamp hours counter.

LAMP_STATE
^^^^^^^^^^

For the ``LAMP_STATE`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``lamp_state``
     - integer
     - Operating state to set the lamp to.

CURVE
^^^^^

For the ``CURVE`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``curve``
     - integer
     - Index of the dimmer curve to set as current.

Raw
^^^

Where a raw PID value has been provided for ``pid``, the ``meta`` object should have a single ``raw`` attribute with a string value. This value will be the base64-encoded string containing parameters for the Set command.

Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format-rdm.rst

Supported RDM PIDs
******************

The following PIDs are directly supported for RDM Set operations:

* ``COMMS_STATUS``
* ``DEVICE_LABEL``
* ``FACTORY_DEFAULTS``
* ``IDENTIFY_DEVICE``
* ``DMX_START_ADDRESS``
* ``DMX_PERSONALITY``
* ``SENSOR_VALUE``
* ``LAMP_HOURS``
* ``LAMP_STATE``
* ``CURVE``
