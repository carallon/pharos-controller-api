RDM Discovery
##############

Returns RDM data from fixtures, or triggers an RDM scan on the desired controller.

HTTP
****

.. _discover-http-get:

GET
===

``GET /api/rdm/discovery``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 5 3 5 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``uid``
     - string
     - manuId:deviceId[:subId]
     - ``"TO DO"``
   * - ``rdm_protocol_version``
     - integer
     - range of 0-65535
     - ``123``
   * - ``device_model_id``
     - integer
     - range of 0-65535
     - ``123``
   * - ``product_category``
     - integer
     - range of 0-65535
     - ``123``
   * - ``software_version_id``
     - integer
     - a 32bit number
     - ``12345678``
   * - ``dmx512_footprint``
     - integer
     - range of 0-512
     - ``3``
   * - ``dmx512_personality``
     - integer
     - range of 0-65535
     - ``2``
   * - ``dmx512_start_address``
     - integer
     - range of 1-512
     - ``4``
   * - ``sub_device_count``
     - integer
     - range of 0-65535
     - ``12``
   * - ``sensor_count``
     - integer
     - range of 0-255
     - ``0``

JavaScript
**********

??? - Not sure how to get this info...?

get_replication
===============

``get_replication(callback)``

Returns an object with the same attributes as in the HTTP GET response.

.. _discover-http-post:

POST
===

``POST /api/rdm/discovery``
Triggers an RDM poll of the defined universe

.. list-table::
   :widths: 3 3 10 5
   :header-rows: 1

   * - Properties
     - Value Type
     - Description
     - Value Example
   * - ``universe``
     - string
     - See `Universe Key String Format`_
     - ``"dmx:1"``


Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format.rst
