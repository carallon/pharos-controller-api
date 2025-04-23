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
   * - ``defaultGateway``
     - IP address
     - The IP address of the default gateway - 0.0.0.0 if none is assigned.
     - ``"192.168.0.1"``
   * - ``ipAddress``
     - IP address
     - The current IP address of the adapter.
     - ``"192.168.0.21"``
   * - ``subnetMask``
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
         "defaultGateway": "192.168.0.1",
         "ipAddress": "192.168.0.21",
         "name": "mgmt",
         "subnetMask": "255.255.255.0"
      }
   ]
