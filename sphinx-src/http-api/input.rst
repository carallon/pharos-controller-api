Input
#####

Methods
*******

GET
===

Returns the status of digital & analogue inputs on the queried controller.

``GET /api/input``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``gpio``
     - array
     - Array of Input objects; returned when queried controller is |LPC| or |TPC| + |EXT|
   * - ``dmxIn``
     - object
     - DMX Input object; returned when DMX input is configured on the queried controller

The Input object has the following properties:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``input``
     - integer
     - Input number
     - ``1``
   * - ``type``
     - string
     - ``Analog``, ``Digital``, or ``Contact Closure``
     - ``"Contact Closure"``
   * - ``value``
     - integer or boolean
     - Value type depends on input type - ``Analog`` inputs return an integer, 0-255; other types return a bool.
     - ``true``

The DMX Input object has the following properties:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``error``
     - string
     - If DMX input is configured but no DMX is received
     - ``"No DMX received"``
   * - ``dmxInFrame``
     - array
     - Array of channel values
     - ``[0,0,0,0,0,0,0,0,0,255,255,255...255,0,255]``
   * - ``dmxInSourceCount``
     - integer
     - The number of sources - will be 1 except for sACN.
     - ``1``
   * - ``dmxInProtocol``
     - string
     - ``dmx``, ``art-net`` or ``sacn``
     - ``"dmx"``

