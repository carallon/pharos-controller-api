Controller
##########

A ``Controller`` object is returned from e.g. :ref:`Lua_get_current_controller`.

Properties
**********

.. list-table::
   :widths: 5 2 8 5
   :header-rows: 1

   * - Property
     - Value Type
     - Description
     - Value Example
   * - ``number``
     - integer
     - Controller number
     - ``1``
   * - ``name``
     - string
     - Controller name
     - ``"Controller 1"``
   * - ``vlan_tag``
     - string
     - VLAN tag number as a string. ``"None"`` if there is no tag set
     - ``"65535"``
   * - ``is_network_primary``
     - boolean
     - Whether this controller is set as the Network Primary in the project
     - ``true``

For example:

.. include:: code-examples/current-controller.rst
