Remote Device
#############

Methods
*******

.. _remote-device-http-get:

GET
===

Returns data about all the remote devices in the project.

``GET /api/remote_device``

Returns a JSON object with a single ``remote_devices`` attribute, which has an array value. Each item in the array is a Remote Device object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Remote device number (address)
     - ``1``
   * - ``type``
     - string
     - ``RIO 08``, ``RIO 44``, ``RIO 80``, ``BPS``, ``BPI``, ``RIO A``, or ``RIO D``
     - ``"RIO 44"``
   * - ``serial``
     - array
     - Array of serial numbers (as strings) of all discovered devices matching the address and type
     - ``["001234","005678"]``
   * - ``outputs``
     - array
     - Array of Output objects (see table below); only returned for RIO 44 and RIO 08 on the queried controller
     - ``[{"output":1,"value":true},{"output":2,"value":true},{"output":3,"value":true},{"output":4,"value":true}]``
   * - ``inputs``
     - array
     - Array of Input objects (see table below); only returned for RIO 44 and RIO 80 on the queried controller
     - ``[{"input":1,"type":"Contact Closure","value":true},{"input":2,"type":"Contact Closure","value":true},{"input":3,"type":"Contact Closure","value":true},{"input":4,"type":"Contact Closure","value":true}]``
   * - ``online``
     - boolean
     - Whether the remote device is detected as being online on the local network
     - ``true``

The Output JSON object has the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``output``
     - integer
     - Number of the output, as labelled on the remote device
     - ``1``
   * - ``state``
     - boolean
     - ``true`` means the output is on, ``false`` means it is off
     - ``true``

The Input JSON object has the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``input``
     - integer
     - Number of the input, as labelled on the remote device
     - ``1``
   * - ``type``
     - string
     - ``Analog``, ``Digital``, or ``Contact Closure``
     - ``""Digital"``
   * - ``value``
     - integer or boolean
     - Value type depends on input type - ``Analog`` inputs return an integer, 0-255; other types return a bool.
     - ``true``
