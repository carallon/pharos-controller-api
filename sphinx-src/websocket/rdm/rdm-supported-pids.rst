RDM Supported PIDs
##################


The following PIDs are supported for decoding within the controller firmware. Other PIDs can still be handled but will not be decoded into JSON fields.

For messages received on the ``rdm_get_set`` channel with ``message_type: result`` and where ``pid`` is a human-readable string, e.g. ``DEVICE_INFO``, the format of the ``data`` object is described in one of the following sections.

Get Communication Status
************************

RDM PID: ``COMMS_STATUS``

For a successful GET operation, the `data` object in the `rdm_get_set` channel `result` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``short_message``
     - number (16 bit)
   * - ``length_mismatch``
     - number (16 bit)
   * - ``checksum_fail``
     - number (16 bit)

Get Status Messages
*******************

RDM PID: ``STATUS_MESSAGES``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``status_messages`` attribute with an array value, the items of which will each have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``sub_device_id``
     - number (16 bit)
   * - ``status_type``
     - number (8 bit)
   * - ``status_message_id``
     - number (16 bit)
   * - ``data_value_1``
     - number (16 bit)
   * - ``data_value_2``
     - number (16 bit)

Get Supported Parameters
************************

RDM PID: ``SUPPORTED_PARAMETERS``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``supported_parameters`` attribute with an array value. The array will contain numbers, corresponding to the 16 bit parameter IDs supported by the RDM device, as described in the RDM specification.

Get Parameter Description
*************************

RDM PID: ``PARAMETER_DESCRIPTION``

For a successful GET operation, the `data` object in the `rdm_get_set` channel `result` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``pid_requested``
     - number (16 bit)
   * - ``pdl_size``
     - number (8 bit)
   * - ``data_type``
     - number (8 bit)
   * - ``command_class``
     - number (8 bit)
   * - ``type``
     - number (8 bit)
   * - ``unit``
     - number (8 bit)
   * - ``prefix``
     - number (8 bit)
   * - ``min_valid_value``
     - number (32 bit)
   * - ``max_valid_value``
     - number (32 bit)
   * - ``default_value``
     - number (32 bit)
   * - ``description``
     - string (ASCII, max 32 characters)

Get Device Info
***************

RDM PID: ``DEVICE_INFO``

For a successful GET operation, the `data` object in the `rdm_get_set` channel `result` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``rdm_protocol_version``
     - number (16 bit)
   * - ``device_model_id``
     - number (16 bit)
   * - ``product_category``
     - number (16 bit)
   * - ``software_version_id``
     - number (32 bit)
   * - ``dmx512_footprint``
     - number (16 bit)
   * - ``dmx512_personality``
     - number (16 bit)
   * - ``start_address``
     - number (16 bit)
   * - ``sub_device_count``
     - number (16 bit)
   * - ``sensor_count``
     - number (8 bit)

Get Device Model Description
****************************

RDM PID: ``DEVICE_MODEL_DESCRIPTION``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``model_description`` attribute with a string value. The string will be the ASCII model description, 0-32 characters, as described in the RDM specification.

Get Manufacturer Label
**********************

RDM PID: ``MANUFACTURER_LABEL``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``manufacturer_label`` attribute with a string value. The string will be the ASCII manufacturer description, 0-32 characters, as described in the RDM specification.


Get/Set Device Label
********************

RDM PID: ``DEVICE_LABEL``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``device_label`` attribute with a string value. The string will be the current ASCII device label, 0-32 characters, as described in the RDM specification.

No data is expected in the response for a SET operation.


Get/Set Factory Defaults
************************

RDM PID: ``FACTORY_DEFAULTS``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``factory_defaults`` attribute with a boolean value, indicating whether the device is currently set to is factory defaults.

No data is expected in the response for a SET operation.


Get Software Version Label
**************************

RDM PID: ``SOFTWARE_VERSION_LABEL``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``software_version_label`` attribute with a string value. The string will be the ASCII software version label, 0-32 characters, as described in the RDM specification.


Get Boot Software Version ID
****************************

RDM PID: ``BOOT_SOFTWARE_VERSION_ID``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``boot_software_version_id`` attribute with a 32 bit number value, as described in the RDM specification.


Get Boot Software Version Label
*******************************

RDM PID: ``BOOT_SOFTWARE_VERSION_LABEL``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``boot_software_version_label`` attribute with a string value. The string will be the ASCII boot version label, 0-32 characters, as described in the RDM specification.


Get/Set DMX512 Personality
**************************

RDM PID: ``DMX_PERSONALITY``

For a successful GET operation, the `data` object in the `rdm_get_set` channel `result` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``current_personality``
     - number (8 bit)
   * - ``num_personalities``
     - number (8 bit)

No data is expected in the response for a SET operation.


Get DMX512 Personality Description
**********************************

RDM PID: ``DMX_PERSONALITY_DESCRIPTION``

For a successful GET operation, the `data` object in the `rdm_get_set` channel `result` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``personality_requested``
     - number (8 bit)
   * - ``dmx512_slots_required``
     - number (16 bit)
   * - ``description``
     - string (ASCII, 0-32 characters)


Get/Set DMX512 Starting Address
*******************************

RDM PID: ``DMX_START_ADDRESS``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``dmx512_address`` attribute with a 16 bit number value, as described in the RDM specification.

No data is expected in the response for a SET operation.

Get Slot Info
*************

RDM PID: ``SLOT_INFO``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have a ``slot_info`` attribute with an array value, the items of which will each have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``slot_offset``
     - number (16 bit)
   * - ``slot_type``
     - number (8 bit)
   * - ``slot_label_id``
     - number (16 bit)

Get Slot Description
********************

RDM PID: ``SLOT_DESCRIPTION``

For a successful GET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``slot_number_requested``
     - number (16 bit)
   * - ``description``
     - string (ASCII, 0-32 characters)

Get Sensor Definition
*********************

RDM PID: ``SENSOR_DEFINITION``

For a successful GET operation, the `data` object in the `rdm_get_set` channel `result` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``sensor_number_requested``
     - number (8 bit)
   * - ``type``
     - number (8 bit)
   * - ``unit``
     - number (8 bit)
   * - ``prefix``
     - number (8 bit)
   * - ``range_minimum_value``
     - number (16 bit)
   * - ``range_maximum_value``
     - number (16 bit)
   * - ``normal_minimum_value``
     - number (16 bit)
   * - ``normal_maximum_value``
     - number (16 bit)
   * - ``recorded_value_support``
     - number (8 bit)
   * - ``description``
     - string (ASCII, 0-32 characters)

Get/Set Sensor Value
********************

RDM PID: ``SENSOR_VALUE``

For a successful GET or SET operation, the ``data`` object in the ``rdm_get_set`` channel ``result`` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``sensor_number_requested``
     - number (8 bit)
   * - ``present_value``
     - number (16 bit)
   * - ``lowest_detected_value``
     - number (16 bit)
   * - ``highest_detected_value``
     - number (16 bit)
   * - ``recorded_value``
     - number (16 bit)

Get/Set Lamp Hours
******************

RDM PID: ``LAMP_HOURS``

For a successful GET or SET operation, the `data` object in the `rdm_get_set` channel `result` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``lamp_hours``
     - number (32 bit)

Get/Set Lamp State
******************

RDM PID: ``LAMP_STATE``

For a successful GET or SET operation, the `data` object in the `rdm_get_set` channel `result` message will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

.. list-table::
   :header-rows: 1

   * - Value
     - Type
   * - ``lamp_state``
     - number (8 bit)
