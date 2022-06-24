System
######

In trigger action scripts the ``system`` namespace is added directly to the environment; in IO modules it is in the ``controller`` namespace, i.e. ``controller.system``.

Properties
**********

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
   * - ``serial_number``
     - string
     - ``"006321"``
   * - ``memory_total``
     - string
     - ``"12790Kb"``
   * - ``memory_used``
     - string
     - ``"24056Kb"``
   * - ``memory_available``
     - string
     - ``"103884Kb"``
   * - ``storage_size``
     - string
     - ``"1914MB"``
   * - ``bootloader_version``
     - string
     - ``"0.9.0"``
   * - ``firmware_version``
     - string
     - ``"2.8.0"``
   * - ``reset_reason``
     - string
     - ``"Software Reset"``
   * - ``last_boot_time``
     - :doc:`date-time`
     - 
   * - ``ip_address``
     - string
     - ``"192.168.1.3"``
   * - ``subnet_mask``
     - string
     - ``"255.255.255.0"``
   * - ``broadcast_address``
     - string
     - ``"192.168.1.255"``
   * - ``default_gateway``
     - string
     - ``"192.168.1.3"``
   * - ``dns_servers``
     - table of strings
     - ``“1.1.1.1”,”1.0.0.1”``

For example:

.. code-block:: lua

   capacity = system.channel_capacity

   boot_time = system.last_boot_time.time_string
