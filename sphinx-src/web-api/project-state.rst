Project State
#############

.. note:: Expert only

HTTP
****

POST
====

Requests a change to a Project State.

``POST /api/project_state``

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - **TODO** Number of the Project State (Is that a thing?)
     - ``"1"``
   * - ``action``
     - string
     - Enum. Currently, only ``set_value`` is supported
     - ``set_value``
   * - ``value_num``
     - string **TODO** Is this right? Why not an int?
     - A string set for the value we want to set the State Value to. **TODO** IS IT 0-255 or 0.0-1.0 or 0-100?
     - ``"189"``