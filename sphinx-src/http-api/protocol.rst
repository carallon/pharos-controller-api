Protocol
########

Methods
*******

.. _protocol-http-get:

GET
===

Returns all the universes in the project on the queried controller.

``GET /api/protocol``

Returns a JSON object with a single ``outputs`` attribute, which has an array value. Each item in the array is a Protocol object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``type``
     - integer
     - Protocol type; possible types are: DMX (1), Pathport (2), Art-Net (4), KiNET (8), sACN (16), DVI (32), RIO DMX (64), |EDN| DMX (128), |EDN| SPI (256)
     - ``1``
   * - ``name``
     - string
     - Protocol name
     - ``"DMX"``
   * - ``disabled``
     - boolean
     - Whether the output has been disabled by a Trigger Action
     - ``false``
   * - ``universes``
     - array
     - Array of Universe objects (see table below)
     - ``[{"key":{"index":1},"name":"1"},{"key":{"index":2},"name":"2"}]``
   * - ``dmx_proxy``
     - object
     - DMX Proxy object, if applicable (see table below)
     - ``{"ip_address":"192.168.1.17","name":"Controller 1"}``

Each Universe object has the following properties:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - A simplistic version of the universe name, which for most protocols is simply the index number
     - ``"1"``
   * - ``key``
     - object
     - Universe Key object (see table below)
     - ``{"index":1}``

Each DMX Proxy object has the following properties:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - Name of the controller that is outputting this universe by proxy
     - ``"Controller 1"``
   * - ``ip_address``
     - string
     - IP address of the controller that is outputting this universe by proxy
     - ``"192.168.1.17"``

The properties of the Universe Key object depend on the type.

For DMX, Pathport, sACN and Art-Net:

.. list-table::
   :widths: 3 3 3
   :header-rows: 1

   * - Attribute
     - Value Type
     - Value Example
   * - ``index``
     - integer
     - ``1``

For KiNET:

.. list-table::
   :widths: 5 3 3
   :header-rows: 1

   * - Attribute
     - Value Type
     - Value Example
   * - ``kinet_port``
     - integer
     - ``1``
   * - ``kinet_power_supply_num``
     - integer
     - ``1``

For RIO DMX:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``remote_device_num``
     - integer
     - Remote device number (address)
     - ``1``
   * - ``remote_device_type``
     - integer
     - Value can be 101 (RIO 80), 102 (RIO 44) or 103 (RIO 08)
     - ``101``

For |EDN|:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``remote_device_num``
     - integer
     - |EDN| number (address)
     - ``1``
   * - ``remote_device_type``
     - integer
     - Value can be 109 (|EDN 20|) or 110 (|EDN 10|)
     - ``110``
   * - ``port``
     - integer
     - Number of |EDN| output port
     - ``1``
