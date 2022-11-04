Time
####

Methods
*******

.. _time-http-get:

GET
===

Returns data about the time stored in the controller.

``GET /api/time``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``datetime``
     - string
     - Controller's local time as a string
     - ``"01 Feb 2017 13:44:42"``
   * - ``local_time``
     - integer
     - Controller's local time in milliseconds
     - ``1485956682``
   * - ``uptime``
     - integer
     - Milliseconds since last boot
     - ``493347``
