Space
#####

.. include:: snippets/endpoints-require-project.rst

Methods
*******

GET
===

Returns data about the spaces in the project and their state on the controller.

``GET /api/space[?num=spaceNum]``

``num`` can be used to filter which space is returned and is expected to be a single number.

Returns a JSON object with a single ``space`` object with the following attributes:

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
   * - ``is_overridden``
     - boolean
     - Whether the space has been overridden.
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
     - ``[{"name":"ChildSpace","num":2,"intensity_master":100,"is_modified":false,...}]``


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
     - The action to perform:

       - ``master_intensity`` sets the space to ``level``.
       - ``off`` recalls scene off in the space.
       - ``activate_relative_scene`` recalls a scene by index within the space.
     - ``"master_intensity"``
   * - ``level``
     - float or string containing a bounded integer
     - Optional - only applies to ``master_intensity``. The master level to apply.
     - ``0.8 or "80:100"``
   * - ``index``
     - integer
     - Optional - only applies to ``activate_relative_scene``. The index of the relative scene to apply, or ``0`` for off.
     - ``7``

For example, to set the intensity master to 42.2% for space 2, the request payload is:

.. code-block:: json

  {
    "num": 2,
    "action": "master_intensity",
    "level": 0.422
  }

For example, to recall the off scene in space 2, the request payload is:

.. code-block:: json

  {
    "num": 2,
    "action": "off"
  }

Relative scene indices are derived by ordering the scenes within a space by scene number.
For example if a space contains scenes 3, 6, 17 and 2 they would map to relative scene numbers like this:


.. list-table::
   :widths: 4 4
   :header-rows: 1

   * - Relative Scene Number
     - Scene Number
   * - 1
     - 2
   * - 2
     - 3
   * - 3
     - 6
   * - 4
     - 17

Number 0 corresponds to off.

So, for example you could activate scene number 6 in the space above using:

.. code-block:: json

  {
    "num": 2,
    "action": "activate_relative_scene",
    "index": 3
  }
