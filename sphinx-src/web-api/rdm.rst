RDM Discovery
#############

Discover RDM fixtures and get cached device info from discovered fixtures.

HTTP
****

.. _discover-http-get:

GET
===

``GET /api/rdm/discovery``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 5 3 8 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``uid``
     - string
     - manuId:deviceId[:subId] (Hex, 4byte:8byte[:decimal integer)
     - ``"072c:0004fe02"``
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

.. _discover-http-post:

POST
====

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
     - See `universe-key-string-format`_ below.
     - ``"dmx:1"``

JavaScript
**********

start_rdm_discovery
===================
``start_rdm_discovery(callback)``

Discover RDM fixtures and get cached device info from discovered fixtures.


RDM PID Information
###################

.. _pid-http-get:

POST
====

``POST /api/rdm/get``
Queues an RDM poll that will return PID information. This is available by subscribing to the relevant websocket. 

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
   * - ``destination_uid``
     - string
     - manuId:deviceId[:subId] (Hex, 4byte:8byte[:decimal integer)
     - ``"072c:0004fe02"``
   * - ``pid`` 
     - string
     - This will request the value for the given PID. See `pid-enums`_ below.
     - ``COMMS_STATUS``
   * - ``meta``
     - object
     - Optional metadata for the PID, i.e. query params.
     - ???

.. _pid-http-set:

``POST /api/rdm/set``
Queues an RDM command that will alter specific PID information. This is available by subscribing to the relevant websocket. 

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
   * - ``destination_uid``
     - string
     - manuId:deviceId[:subId] (Hex, 4byte:8byte[:decimal integer)
     - ``"072c:0004fe02"``
   * - ``pid`` 
     - string
     - This will be the PID we intend to change. See `pid-enums`_ below.
     - ``COMMS_STATUS``
   * - ``meta``
     - object
     - Optional metadata for the PID, i.e. query params.
     - ???

??? HOW IS THE PID INFO SET?

JavaScript
**********

start_rdm_get
=============
``start_rdm_get(params, callback)``

Returns chosen PID information from the selected fixture.

``params`` is expected to be an object with the following attributes:

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
   * - ``destination_uid``
     - string
     - manuId:deviceId[:subId] (Hex, 4byte:8byte[:decimal integer)
     - ``"072c:0004fe02"``
   * - ``pid`` 
     - string
     - This will request the value for the given PID. See `pid-enums`_ below.
     - ``COMMS_STATUS``
   * - ``meta``
     - object
     - Optional metadata for the PID, i.e. query params.
     - ???

start_rdm_set
=============
``start_rdm_set(params, callback)``

Sets PID value for the selected fixture.

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
   * - ``destination_uid``
     - string
     - manuId:deviceId[:subId] (Hex, 4byte:8byte[:decimal integer)
     - ``"072c:0004fe02"``
   * - ``pid`` 
     - string
     - This will request the value for the given PID. See `pid-enums`_ below.
     - ``COMMS_STATUS``
   * - ``meta``
     - object
     - Optional metadata for the PID, i.e. query params.
     - ???

??? DO WE NEED TO GIVE EXAMPLES OF WHAT TO USE FOR CALLBACK?

Universe Key String Format
**************************
.. _universe-key-string-format:
.. include:: ../snippets/universe-key-string-format.rst

PID Enums
*********
.. _pid-enums:
.. include:: ../snippets/pid-enums.rst
