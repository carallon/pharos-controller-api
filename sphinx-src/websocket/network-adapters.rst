Network Adapters
################

The Network Adapters call returns an array of the network adapters on the target controller. Each adapter includes the following properties:

.. list-table::
   :widths: 3 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``capturing``
     - boolean
     - Whether the adapter is currently executing a network capture
     - ``false``
   * - ``connected``
     - boolean
     - Whether the adapter is currently connected.
     - ``true``
   * - ``default_gateway``
     - IP address
     - The IP address of the default gateway - 0.0.0.0 if none is assigned.
     - ``"192.168.0.1"``
   * - ``ip_address``
     - IP address
     - The current IP address of the adapter.
     - ``"192.168.0.21"``
   * - ``mac_address``
     - MAC address
     - The hardware address of the adapter.
     - ``"00:1A:2B:3C:4D:5E"``
   * - ``subnet_mask``
     - IP address
     - The subnet mask of the adapter in dotted-decimal format.
     - ``"255.255.255.0"``
   * - ``name``
     - string
     - The system name of the adapter.
     - ``"mgmt"``

For example:

.. code-block:: json

   "adapters": [
      {
         "capturing": false,
         "connected": true,
         "default_gateway": "192.168.0.1",
         "ip_address": "192.168.0.21",
         "mac_address": "00:1A:2B:3C:4D:5E",
         "name": "mgmt",
         "subnet_mask": "255.255.255.0"
      }
   ]
