RDM Device Info
###############

Where an RDM Device Info object is returned from an API request, it will have the following attributes:

.. list-table::
   :widths: 5 2 10 4
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``uid``
     - string
     - Format is ``{manuId}:{deviceId}(:{subId})``
       where ``{manuId}`` is a padded unsigned hexadecimal integer of width 4, lowercase, e.g. ``072c``;
       ``{deviceId}`` is a padded unsigned hexadecimal integer of width 8, lowercase, e.g. ``0004fe02``;
       ``{subId}`` is an optional unsigned decimal integer.
     - ``"072c:0004fe02"``
   * - ``rdm_protocol_version``
     - integer
     - 16 bit value encoding the major version in the most significant byte and the minor version in the least significant byte. The current standard v1.0 is therefore ``0x0100``.
     - ``0x0100``
   * - ``device_model_id``
     - integer
     - Device model ID of the Root Device or the Sub-Device. Must be unique within the products of a manufacturer.
     - ``1836``
   * - ``product_category``
     - integer
     - 16 bit value encoding the coarse category in the upper eight bits and the (optional) fine category in lower eight bits, e.g. ``0x0100`` is ``PRODUCT_CATEGORY_FIXTURE`` with no fine category.
     - ``0x0100``
   * - ``software_version_id``
     - integer
     - Software version ID for the device, which is a 32-bit value determined by the manufacturer. It may use any encoding scheme such that the controller may identify devices containing the same software versions. Any devices from the same manufacturer with differing software will not report the same software version ID.
     - 
   * - ``dmx512_footprint``
     - integer (0-512)
     - The DMX footprint of the device - the number of consecutive DMX slots required to patch the device. If the device is a sub-device, then the value is the DMX footprint for that sub-device. If the device is the root device, it is the footprint for the root device itself.
     - ``3``
   * - ``dmx512_personality``
     - integer
     - 16 bit field, encoding the current personality in the upper 8 bits and the total number of personalities supported by the device in the lower 8 bits.
     - ``0x0102``
   * - ``dmx512_start_address``
     - integer
     - The DMX start address of the device, or ``0xffff`` if the device has a DMX footprint of zero.
     - ``7``
   * - ``sub_device_count``
     - integer
     - Number of sub devices represented by the root device. This value is always the same regardless of whether the device is the root device or a sub-device.
     - ``0``
   * - ``sensor_count``
     - integer
     - Number of available sensors in a root device or sub-device. For sub-devices, this value is identical for any sub-device owned by the same root device. When a device or sub-device is fitted with a single sensor, it will return a value of 0x01 for the sensor count. This sensor would then be addressed as sensor number 0x00 when using the other sensor-related parameter messages.
     - ``0``
