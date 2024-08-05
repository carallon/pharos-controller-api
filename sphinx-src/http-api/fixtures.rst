.. _fixtures:

Fixtures
########

All properties described below relating to a fixture or device's status are obtained by the :ref:`status-monitor`.

Fixtures Overview
*****************

.. _fixtures-overview-http-get:

GET
===

Get an overview of fixtures used in the current project including their statuses.

``GET /api/fixtures``

Returns a JSON array of objects with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``groups``
     - array of strings
     - Names of groups containing this fixture
     - ``["1 All Exterior"]``
   * - ``manufacturer``
     - string
     - Manufacturer name as defined in the fixture library
     - ``"Generic"``
   * - ``number``
     - integer
     - User number of the fixture
     - ``1``
   * - ``patch``
     - string
     - Combined universe key and address (see `Universe Key String Format`_)
     - ``"dmx:2:101"``
   * - ``protocol``
     - string
     - ``"dali"``, or ``"dmx"``
     - ``"dmx"``
   * - ``status``
     - string
     - ``"online"``, ``"partially_offline"``, ``"offline"``, ``"loading"``, or ``null`` if unknown
     - ``"online"``
   * - ``updated_at``
     - string
     - ISO 8601-formatted timestamp of the last status update, or ``null`` is unknown
     - ``2024-06-27T09:30``

Fixture
*******

GET
===

Get detailed information for a single fixture including its status.

``GET /api/fixtures/{fixtureNumber}``

Returns a JSON object extending the :ref:`Fixtures Overview GET <fixtures-overview-http-get>` response with the following additional attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``type``
     - string
     - Fixture type as defined in the fixture library
     - ``LED - RGBW 8 bit``
   * - ``rdm_device_uids``
     - array of strings
     - The UIDs of any RDM devices associated with this fixture
     - ``["1234:56789abc"]``
   * - ``custom_properties``
     - object
     - Object properties and property values correspond to custom property names and values
     - ``{ "Custom Property 1": "value" }``

Fixture Devices
***************

.. _fixture-devices-http-get:

GET
===

Get an overview of a fixture's physical devices including their statuses.

``GET /api/fixtures/{fixtureNumber}/devices``

Returns a JSON array of objects with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``uid``
     - string
     - RDM device UID
     - ``"1234:56789abc"``
   * - ``patch``
     - string
     - Combined universe key and address (see `Universe Key String Format`_)
     - ``"dmx:2:101"``
   * - ``rdm``
     - object
     - RDM parameters cached from the latest status monitor run
     - ``{}``
   * - ``status``
     - string
     - ``"online"``, ``"offline"``, ``"loading"``, or ``null`` if unknown
     - ``"online"``
   * - ``updated_at``
     - string
     - ISO 8601-formatted timestamp of the last status update, or ``null`` if unknown
     - ``2024-06-27T09:30``

Fixture Device
**************

GET
===

Get a single physical device for a fixture including its status.

``GET /api/fixtures/{fixtureNumber}/device/{deviceId}``

Returns a JSON object with the same properties as contained in the :ref:`Fixture Devices GET <fixture-devices-http-get>` response.

Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format.rst
