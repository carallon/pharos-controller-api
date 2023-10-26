Tag Set
#######

Methods
*******

GET
===

Returns data about the Tag Sets in the project and their state on the controller.

``GET /api/tag_set``

Returns a JSON object with a single ``tag_sets`` attribute, which has an array value. Each item in the array is a Tag Set object with the following attributes:

.. list-table::
   :widths: 3 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Tag Set number
     - ``1``
   * - ``name``
     - string
     - Tag Set name
     - ``"Season"``
   * - ``is_editable``
     - boolean
     - Whether the Tag Set can be manually overridden from control panels
     - ``false``
   * - ``tags``
     - array of objects
     - An array of Tag objects. Each Tag object has a ``name`` and ``num`` property
     - ``{{"name":"Spring","num":1}, {"name":"Summer","num":2}}``
   * - ``active_tag``
     - object
     - The currently active Tag in the Tag Set
     - ``{"name":"Spring","num":1}``


POST
====

Allows tag sets to be controlled.

``POST /tag_set``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``num``
     - integer
     - The target tag set number.
   * - ``action``
     - string
     - The action to perform on the tag set. ``set_tag`` is the only currently supported action.
   * - ``tag_num``
     - integer
     - The target tag number .