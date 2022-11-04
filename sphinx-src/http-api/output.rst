Output
######

Methods
*******

POST
====

Enable/disable the output of a selected protocol from the controller. Action will propagate to all controllers in a project.

``POST /api/output``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
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

.. _output-http-get:

GET
===

Returns the lighting levels being output by the queried controller.

``GET /api/output?universe=universeKey``

``universeKey`` is a string; see `Universe Key String Format`_.

For example:
* ``GET /api/output?universe=dmx:1``
* ``GET /api/output?universe=rio-dmx:rio44:1``

If the queried controller is an |LPC| 1, the universe is DMX 2, DMX Proxy has been enabled for a |TPC| in the project and the |TPC| is offline then this request will return a JSON object with the following attributes:

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
   :widths: 5 2 10 5
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

Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format.rst
