Current RDM implementation supports the following PIDs:

**TODO** Data still needs to be retrieved from https://wiki.office.carallon.com/Programmes/Magpie/RdmPolling#RdmParameterDescription.

.. list-table::
   :widths: 2 3 3
   :header-rows: 1
   :align: left

   * - PID String
     - GET data
     - SET metadata
   * - ``"COMMS_STATUS"``
     - Comms Status object
     - SET
   * - ``"STATUS_MESSAGES"``
     - Array of Status Message
     - SET
   * - ``"SUPPORTED_PARAMETERS"``
     - Array of integers
     - SET
   * - ``"PARAMETER_DESCRIPTION"``
     - Parameter Description
     - SET
   * - ``"DEVICE_INFO"``
     - Device Info
     - SET
   * - ``"DEVICE_MODEL_DESCRIPTION"``
     - string
     - SET
   * - ``"MANUFACTURER_LABEL"``
     - string
     - SET
   * - ``"DEVICE_LABEL"``
     - string
     - SET
   * - ``"FACTORY_DEFAULTS"``
     - boolean
     - SET
   * - ``"SOFTWARE_VERSION_LABEL"``
     - string
     - SET
   * - ``"BOOT_SOFTWARE_VERSION_ID"``
     - integer
     - SET
   * - ``"BOOT_SOFTWARE_VERSION_LABEL"``
     - string
     - SET
   * - ``"DMX_PERSONALITY"``
     - Personality
     - SET
   * - ``"DMX_PERSONALITY_DESCRIPTION"``
     - Personality Description
     - SET
   * - ``"DMX_START_ADDRESS"``
     - integer
     - SET
   * - ``"SLOT_INFO"``
     - Array of Slot Info
     - SET
   * - ``"SLOT_DESCRIPTION"``
     - Slot Description
     - SET
   * - ``"SENSOR_DEFINITION"``
     - Sensor Definition
     - SET
   * - ``"SENSOR_VALUE"``
     - Sensor Value
     - SET