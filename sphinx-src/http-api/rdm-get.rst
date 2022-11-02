RDM Get
#######

Methods
*******

.. _rdm-get-http-post:

POST
====

Request to start an RDM Get operation. A ``202`` response will be returned if the request has been successfully queued. Results are available via a websocket subscription (see :ref:`websocket_subscribe_rdm_get_set`).

``POST /api/rdm/get``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 2 5 5 3
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``universe``
     - string in `Universe Key String Format`_ or :doc:`objects/rdm-universe-key`
     - The universe on which to perform the RDM Get operation.
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
     - RDM PID for the Get operation. Can be one of the `Supported RDM PIDs`_ or the raw PID value as a hex string, e.g. ``"FF"``.
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

STATUS_MESSAGES
^^^^^^^^^^^^^^^

For the ``STATUS_MESSAGES`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 5 2 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``status_type``
     - integer
     - Type of status messages to retrieve. Set to STATUS_NONE (``0x00``) to establish whether a device is present on the network without retrieving any status message data from the device.

PARAMETER_DESCRIPTION
^^^^^^^^^^^^^^^^^^^^^

For the ``PARAMETER_DESCRIPTION`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 5 2 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``pid_requested``
     - integer
     - The manufacturer-specific PID for which a description is requested. Range 0x8000 to 0xFFDF.

DMX_PERSONALITY_DESCRIPTION
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the ``DMX_PERSONALITY_DESCRIPTION`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 5 2 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``personality_requested``
     - integer
     - Index of the requested personality.

SLOT_DESCRIPTION
^^^^^^^^^^^^^^^^

For the ``SLOT_DESCRIPTION`` PID, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 4
   :header-rows: 1

   * - Attribute
     - Value Type
   * - ``slot_number_requested``
     - integer

SENSOR_DEFINITION and SENSOR_VALUE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the ``SENSOR_DEFINITION`` and ``SENSOR_VALUE`` PIDs, the ``meta`` object should have the following parameters:

.. list-table::
   :widths: 4 4
   :header-rows: 1

   * - Attribute
     - Value Type
   * - ``sensor_number_requested``
     - integer

Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format-rdm.rst

Supported RDM PIDs
******************

The following PIDs are directly supported for RDM Get operations:

* ``COMMS_STATUS``
* ``STATUS_MESSAGES``
* ``SUPPORTED_PARAMETERS``
* ``PARAMETER_DESCRIPTION``
* ``DEVICE_INFO``
* ``DEVICE_MODEL_DESCRIPTION``
* ``MANUFACTURER_LABEL``
* ``DEVICE_LABEL``
* ``FACTORY_DEFAULTS``
* ``SOFTWARE_VERSION_LABEL``
* ``BOOT_SOFTWARE_VERSION_ID``
* ``BOOT_SOFTWARE_VERSION_LABEL``
* ``DMX_PERSONALITY``
* ``DMX_PERSONALITY_DESCRIPTION``
* ``DMX_START_ADDRESS``
* ``SLOT_INFO``
* ``SLOT_DESCRIPTION``
* ``SENSOR_DEFINITION``
* ``SENSOR_VALUE``
* ``LAMP_HOURS``
* ``LAMP_STATE``
