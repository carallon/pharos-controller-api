Temperature
###########

Methods
*******

.. _temperature-http-get:

GET
===

Returns data about the controller's temperature.

``GET /api/temperature``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``sys_temp``
     - number
     - Only for |LPC X| and |VLC|/|VLC+|
     - ``40.2``
   * - ``core1_temp``
     - number
     - Only for |LPC X| and |VLC|/|VLC+|
     - ``44``
   * - ``core2_temp``
     - number
     - Only for |LPC X| rev 1
     - ``44.1``
   * - ``ambient_temp``
     - number
     - Only for |TPC|, |LPC X| rev 1
     - ``36.9``
   * - ``cc_temp``
     - number
     - Only for |LPC X| rev 2 and |VLC|/|VLC+|
     - ``44.1``
   * - ``gpu_temp``
     - number
     - Only for |VLC|/|VLC+|
     - ``38.2``
