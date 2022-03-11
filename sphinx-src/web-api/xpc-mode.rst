Expert Control Mode
###################
.. note:: Expert only

HTTP
****

GET
===

Gets the current mode dial position

``GET /api/mode``

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``mode``
     - string
     - Enum; see options listed below
     - ``"Run"``

Expert Control Dial Enums
*************************

``Run``, ``Dmx1``, ``Dmx2``, ``Dali``, ``All``, ``Off``, ``PG1``, ``PG2``, ``PG3``, ``PG4``
