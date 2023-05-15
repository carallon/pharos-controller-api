Space
#####

Methods
*******

GET
===

Returns data about the spaces in the project and their state on the controller.

``GET /api/space[?num=spaceNum]``

``num`` can be used to filter which spaces are returned and is expected to be either a single number or a string expressing the required spaces, e.g. ``"1,2,5-9"``.

Returns a JSON object with a single ``spaces`` attribute, which has an array value. Each item in the array is a Space object with the following attributes:

.. list-table::
   :widths: 3 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Space number
     - ``1``
   * - ``name``
     - string
     - Space name
     - ``"Space 1"``
   * - ``is_modified``
     - boolean
     - Whether the space has been modified.
     - ``false``
   * - ``intensity_master``
     - integer
     - The current intensity master value for the space
     - ``100``
   * - ``active_scene``
     - object
     - The current active scene in the space
     - ``{"name":"Off","num":0}``
   * - ``child_scenes``
     - array of objects
     - A list of the available scenes in the space.
     - ``[{"name":"Off","num":0},{"name":"Full","num":1}]``
   * - ``child_spaces``
     - array of objects
     - A list of the child spaces of this space.
     - ``[{"name":"ChildSpace","num":0}]``


POST
====

Control a space in the project.

``POST /api/space``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - string
     - The space number to perform the action on.
     - ``2``
   * - ``action``
     - string
     - The action to perform. Currently ``master_intensity`` is the only supported action.
     - ``"master_intensity"``
   * - ``level``
     - number
     - Optional. The master level to apply, in percent.
     - ``80``

For example, to set the intensity master to 42.2% for space 2, the request payload is:

.. code-block:: json

  {
    "num": 2,
    "action": "master_intensity",
    "level": 42.2
  }
