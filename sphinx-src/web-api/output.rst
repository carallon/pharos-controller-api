Output
######


HTTP
****

POST
====

Enable/disable the output of a selected protocol from the controller.

``POST /api/output``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``protocol``
     - string
     - Protocol to disable. Options: ``dmx``, ``pathport``, ``sacn``, ``art-net``, ``kinet``, ``rio-dmx``, ``edn``, ``edn-spi``.
     - ``"parthport"``
   * - ``action``
     - string
     - Whether to ``enable`` or ``disable`` output via the protocol.
     - ``"disable"``

GET
===

Returns the lighting levels being output by the queried controller.

``GET /api/output?universe=universeKey``

``universeKey`` is a string; see `Universe Key String Format`_.

For example:
* ``GET /api/output?universe=dmx:1``
* ``GET /api/output?universe=rio-dmx:rio44:1``

If the queried controller is an LPC 1, the universe is DMX 2, DMX Proxy has been enabled for a TPC in the project and the TPC is offline then this request will return a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Value Example
   * - ``proxied_tpc_name``
     - string
     - ``"Controller 2""``

Otherwise a JSON object with the following attributes is returned:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``channels``
     - array
     - Array of integer (0-255) channel levels
     - ``[0,0,0,0,0,0,0,0,0,255,255,255...255,0,255]``
   * - ``disabled``
     - bool
     - Whether the output has been disabled by a Trigger Action
     - ``false``

JavaScript
**********

disable_output
==============

Disable the output of a specified protocol from the controller.

``disable_output(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``protocol``
     - string
     - Protocol to disable. Options: ``dmx``, ``pathport``, ``sacn``, ``art-net``, ``kinet``, ``rio-dmx``, ``edn``, ``edn-spi``.
     - ``"parthport"``

enable_output
=============

Enable the output of a specified protocol from the controller.

``enable_output(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``protocol``
     - string
     - Protocol to enable. Options: ``dmx``, ``pathport``, ``sacn``, ``art-net``, ``kinet``, ``rio-dmx``, ``edn``, ``edn-spi``.
     - ``"parthport"``

get_output
==========

Returns the lighting levels being output by the queried controller.

``get_output(universeKey, callback)``

Returns an object with the same attributes as in the HTTP GET response.

``universeKey`` can be a string (see `Universe Key String Format`_) or it can be an object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``protocol``
     - integer
     - Constants defined in query.js are: ``DMX`` (1), ``PATHPORT`` (2), ``ARTNET`` (4), ``KINET`` (8), ``SACN`` (16), ``DVI`` (32), ``RIO_DMX`` (64), ``EDN`` (128)
   * - ``index``
     - integer
     - Required unless ``protocol`` is ``KINET``, ``RIO_DMX`` or ``EDN``
   * - ``kinet_power_supply_num``
     - integer
     - Only required if ``protocol`` is ``KINET``
   * - ``kinet_port``
     - integer
     - Only required if ``protocol`` is ``KINET``
   * - ``remote_device_type``
     - integer
     - Only required if ``protocol`` is ``RIO_DMX`` or ``EDN``
   * - ``remote_device_num``
     - integer
     - Only required if ``protocol`` is ``RIO_DMX`` or ``EDN``
   * - ``port``
     - integer
     - Only required if ``protocol`` is ``EDN``

For example:

.. code-block:: js

   Query.get_output({
       protocol: KINET,
       kinet_port: 1,
       kinet_power_supply_num: 1
     }, u => {
     console.log(u)
     }
   )

   Query.get_output({
       protocol: DMX,
       index: 1
     }, u => {
       console.log(u)
     }
   )

   Query.get_output("dmx:1", u => {
     console.log(u)
   })

Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format.rst