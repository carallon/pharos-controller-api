Mode Switch
###########

Methods
*******

GET
===

Returns the position of the rotary dial on the front of the Expert controller.

``GET /api/mode``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``mode``
     - string
     - The mode switch position. One of: ``RUN``, ``PG1``, ``PG2``, ``PG3``, ``PG4``, ``ALL``, ``DALI``, ``DX2``, ``DX1``, ``OFF``
