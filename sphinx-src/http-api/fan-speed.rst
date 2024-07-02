Fan Speed
##########

Methods
*******

.. _fan-speed-http-get:

GET
===

Returns data about the controller's fan speeds.

``GET /api/fan_speed``

Returns a JSON object with a single ``fan_speed`` attribute, which has either a boolean ``false`` value if the controller has no fans or a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``fan_1``
     - integer
     - The speed of the left-hand fan in RPM 
     - ``2368``
   * - ``fan_2``
     - integer
     - The speed of the right-hand fan in RPM 
     - ``3605``

