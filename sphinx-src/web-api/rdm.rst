RDM Discovery
#############

Discover RDM fixtures and get cached device info from discovered fixtures.

HTTP
****

.. _rdm-discover-http-get:

GET
===

``GET /api/rdm/discovery``

Returns an array with the following attributes:

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
     - Range of 0-65535
     - ``123``
   * - ``device_model_id``
     - integer
     - Range of 0-65535
     - ``123``
   * - ``product_category``
     - integer
     - Range of 0-65535
     - ``123``
   * - ``software_version_id``
     - integer
     - A 32bit number
     - ``12345678``
   * - ``dmx512_footprint``
     - integer
     - Range of 0-512
     - ``3``
   * - ``dmx512_personality``
     - integer
     - Range of 0-65535
     - ``2``
   * - ``dmx512_start_address``
     - integer
     - Range of 1-512
     - ``4``
   * - ``sub_device_count``
     - integer
     - Range of 0-65535
     - ``12``
   * - ``sensor_count``
     - integer
     - Range of 0-255
     - ``0``

.. _rdm-discover-http-post:

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
     - See `Universe Key String Format`_
     - ``"dmx:1"``

JavaScript
**********

start_rdm_discovery
===================

``start_rdm_discovery(params, callback)``

Discover RDM fixtures and get cached device info from discovered fixtures.

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
     - See `RDM UIDs`_
     - ``"072c:0004fe02"``
   * - ``pid`` 
     - string
     - This will request the value for the given PID. See `PID Enums`_ below.
     - ``"COMMS_STATUS"``
   * - ``meta``
     - object
     - Optional metadata for the PID, i.e. query params.
     - **TODO**

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
     - See `RDM UIDs`_
     - ``"072c:0004fe02"``
   * - ``pid`` 
     - string
     - This will be the PID we intend to change. See `PID Enums`_ below.
     - ``"COMMS_STATUS"``
   * - ``meta``
     - object
     - Optional metadata for the PID, i.e. query params.
     - **TODO**

**TODO** HOW IS THE PID INFO SET?

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
     - See `RDM UIDs`_
     - ``"072c:0004fe02"``
   * - ``pid`` 
     - string
     - This will request the value for the given PID. See `PID Enums`_ below.
     - ``COMMS_STATUS``
   * - ``meta``
     - object
     - Optional metadata for the PID, i.e. query params.
     - **TODO**

start_rdm_set
=============

``start_rdm_set(params, callback)``

Sets PID value for the selected fixture.

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
     - See `RDM UIDs`_
     - ``"072c:0004fe02"``
   * - ``pid`` 
     - string
     - This will request the value for the given PID. See `PID Enums`_ below.
     - ``COMMS_STATUS``
   * - ``meta``
     - object
     - Optional metadata for the PID, i.e. query params.
     - **TODO**

**TODO** DO WE NEED TO GIVE EXAMPLES OF WHAT TO USE FOR CALLBACK?

Universe Key String Format
**************************
.. _universe-key-string-format:
.. include:: ../snippets/universe-key-string-format.rst

PID Enums
*********
.. _pid-enums:
.. include:: ../snippets/pid-enums.rst

RDM UIDs
********
.. _rdm-uids:

RDM UIDs is a hexidecimal value take the format:

``manuId:deviceId[:subId]`` 

where each value is set as follows:

.. list-table::
   :widths: 3 3
   :header-rows: 1
   :align: left

   * - ID
     - Type
   * - ``manuId``
     - 4-byte
   * - ``deviceId``
     - 8-byte
   * - ``subId``
     - Decimal Integer (optional)

For example:

.. code-block:: none

   072c:0004fe02:2


  


