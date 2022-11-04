Channel / Park
##############

Methods
*******

.. _channel-http-post:

POST
====

Park an output channel or channels at a specified level.

``POST /api/channel``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``universe``
     - string
     - See `Universe Key String Format`_
     - ``"dmx:1"``
   * - ``channels``
     - string
     - Comma separated list of channel numbers.
     - ``"1-3,5"``
   * - ``level``
     - integer
     - Level to set the channel(s) to: 0-255.
     - ``128``

.. _channel-http-delete:

DELETE
======

Unpark an output channel or channels.

``DELETE /api/channel``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``universe``
     - string
     - See `Universe Key String Format`_
     - ``"dmx:1"``
   * - ``channels``
     - string
     - Comma separated list of channel numbers.
     - ``"1-3,5"``

Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format.rst
