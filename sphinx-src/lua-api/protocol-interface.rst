Network 2
#########

Information about the controller's second network interface is available in the ``protocol_interface`` namespace. In trigger action scripts the ``protocol_interface`` namespace is added directly to the environment; in IO modules it is in the ``controller`` namespace, i.e. ``controller.protocol_interface``.

Properties
**********

The ``protocol_interface`` namespace has the following properties:

.. list-table::
   :widths: 3 2 5
   :header-rows: 1

   * - Property
     - Value Type
     - Value Example
   * - ``has_interface``
     - boolean
     - ``true``
   * - ``is_up``
     - boolean
     - ``true``
   * - ``ip_address``
     - string
     - ``"192.168.1.12"``
   * - ``subnet_mask``
     - string
     - ``"255.255.255.0"``
   * - ``gateway``
     - string
     - ``"192.168.1.1"``

For example:

.. code-block:: lua

   if protocol_interface.has_interface == true then
     ip = protocol_interface.ip_address
   end
