Expert Control Mode
###################

.. note:: Expert only

HTTP
****

GET
===

Gets the current mode dial position.

``GET /api/mode``

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1
   :align: left

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``mode``
     - string
     - Enum; see `Expert Control Dial Enums`_
     - ``Run``

Expert Control Dial Enums
*************************

.. list-table::
   :widths: 3 10
   :header-rows: 1
   :align: left
   
   * - Enum
     - Description 
   * - ``Run``
     - Runs normal operation for the controller.
   * - ``Dmx1``
     - Test mode for DMX port 1.
   * - ``Dmx2``
     - Test mode for DMX port 2.
   * - ``Dali``
     - Test mode for DALI port.
   * - ``All``
     - Tests all output ports.
   * - ``Off``
     - Ceases all output.
   * - ``PG1``
     - Same as ``Run`` with State Value "PG1" active.
   * - ``PG2``
     - Same as ``Run`` with State Value "PG2" active.
   * - ``PG3``
     - Same as ``Run`` with State Value "PG3" active.
   * - ``PG4``
     - Same as ``Run`` with State Value "PG4" active.
