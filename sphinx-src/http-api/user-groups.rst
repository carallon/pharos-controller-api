User Groups
###########

These methods allow discovery of the user and guest groups on the controller.

Methods
*******

GET
===

``GET /api/user_groups``

Get the list of available user groups. Returns a JSON object with the following attributes:

.. list-table::
   :widths: 4 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``user_groups``
     - array of strings
     - The list of available groups.
     - ``["Admin", "Control", "Status"]``

GET
===

``GET /api/guest_groups``

Get the list of available guest groups. Returns a JSON object with the following attributes:

.. list-table::
   :widths: 4 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``guest_groups``
     - array of strings
     - The list of available guest groups.
     - ``["Foo", "Bar"]``
