Space
#####
.. note:: Expert only

HTTP
****

GET
===

Returns information on a given Space.

``GET /api/space``

Returns a JSON object with a single ``space`` attribute, which has an array value. Each item in the array is a Space object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - Space name
     - ``"Space 1"``
   * - ``num``
     - integer
     - Space number
     - ``1``
   * - ``intensity_master``
     - integer
     - **TODO** 0-255 VALUE?
     - ``189``
   * - ``active_scene``
     - object
     - Contains ``name`` (str) and ``num`` (int)
     - **TODO**
   * - ``is_modified``
     - boolean
     - **TODO** Checks if the space is currently overridden 
     - ``true``
   * - ``child_spaces``
     - array
     - Contains an array of all child spaces, each an object using the same format as the ``space`` object.
     - **TODO**
   * - ``child_scenes``
     - array
     - Contains an array of all scenes on child spaces, in the same format as ``active_scene``
     - **TODO**


POST
====

Triggers intensity mastering on the selected Space.

``POST /api/space``

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Space number
     - ``"1"``
   * - ``action``
     - string
     - Enum. Currently, only master intensity is supported
     - ``"master_instensity"``
   * - ``level``
     - string **TODO** < IS THAT RIGHT? WHY NOT AN INT?
     - A string set for the value we want to set the master to. ??? IS IT 0-255 or 0.0-1.0 or 0-100?
     - ``"189"``