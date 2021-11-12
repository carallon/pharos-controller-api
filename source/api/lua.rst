Lua API
#######

The Lua API is available in the trigger script environment and in IO modules under the `controller` namespace.

System
******

The ``system`` namespace has the following properties:

.. list-table::
   :widths: 3 2 5
   :header-rows: 1

   * - Property
     - Value Type
     - Value Example
   * - ``hardware_type``
     - string
     - ``"lpc"``
   * - ``channel_capacity``
     - integer
     - ``512``
   * - ``etc``
     - etc
     - **To do:** complete table


For example:

.. code-block:: lua

   capacity = system.channel_capacity

   boot_time = system.last_boot_time.time_string

Project
*******

``get_current_project()``

Returns an object with the following properties:

.. list-table::
   :widths: 3 2 5
   :header-rows: 1

   * - Property
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


For example:

.. code-block:: lua

   project_name = get_current_project().name
