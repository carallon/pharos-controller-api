System
######

Returns data about the controller.

HTTP
****

GET
===

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
   * - ``serial_number``
     - string
     - ``"006321"``
   * - ``memory_total``
     - string
     - ``"12790Kb"``
   * - ``memory_used``
     - string
     - ``"24056Kb"``
   * - ``memory_free``
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
     - string
     - ``"01 Jan 2017 09:09:38"``
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

JavaScript
**********

get_system_info
===============

``get_system_info(callback)``

Returns an object with the same attributes as in the HTTP GET response.

For example:

.. code-block:: js

   Query.get_system_info(system => {
     const capacity = system.channel_capacity
   })
