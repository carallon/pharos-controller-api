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
     - The action to perform. ``master_intensity`` sets the space to ``level``. ``off`` recalls scene off in the space.
     - ``"master_intensity"``
   * - ``level``
     - float or string containing a bounded integer
     - Optional. The master level to apply.
     - ``0.8 or "80:100"``

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
