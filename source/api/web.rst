Web API
#######

System
******

Returns data about the controller.

HTTP
====

GET
---

``GET /api/system``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 3 2 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Value Example
   * - ``hardware_type``
     - string
     - ``"LPC"``
   * - ``channel_capacity``
     - integer
     - ``512``
   * - ``etc``
     - etc
     - **To do:** complete table

JavaScript
==========

``get_system_info(callback)``

Returns an object with the same attributes as in the HTTP GET response.

For example:

.. code-block:: js

   Query.get_system_info(function(system) {
     var capacity = system.channel_capacity
   }

Project
*******

Returns data about the current project.

HTTP
====

GET
---

``GET /api/project``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 3 2 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Value Example
   * - ``name``
     - string
     - ``"Help Project"``
   * - ``author``
     - string
     - ``"Pharos"``
   * - ``etc``
     - etc
     - **To do:** complete table

JavaScript
==========

``get_project_info(callback)``

Returns an object with the same attributes as in the HTTP GET response.

For example:

.. code-block:: js

   Query.get_project_info(function(project) {
     var author = project.author
   }
