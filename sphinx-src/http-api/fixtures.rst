.. _fixtures:

Fixtures
########

.. include:: snippets/endpoints-require-project.rst

All properties described below relating to a fixture or device's status are obtained by the :ref:`status-monitor`.

Fixtures Overview
*****************

.. _fixtures-overview-http-get:

GET
===

Get an overview of fixtures used in the current project including their statuses.

``GET /api/fixtures``

Returns a JSON array of objects with the following attributes:

.. only:: designer

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
    * - ``issues``
      - array of strings
      - Issue keys collected from devices patched to this fixture (see :ref:`RDM Device Issues <rdm-devices-device-issues>`)
      - ``["address_mismatch"]``
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
      - ``"online"``, ``"partially_offline"``, ``"offline"``, ``"loading"``, or ``"unknown"``
      - ``"online"``
    * - ``type``
      - string
      - Fixture type as defined in the fixture library
      - ``LED - RGBW 8 bit``
    * - ``updated_at``
      - string
      - ISO 8601-formatted timestamp of the last status update, or ``null`` if unknown
      - ``2024-06-27T09:30``

.. only:: expert

  .. list-table::
    :widths: 5 2 10 5
    :header-rows: 1

    * - Attribute
      - Value Type
      - Description
      - Value Example
    * - ``space``
      - string
      - Name of the immediate parent space containing this fixture
      - ``"1: Project Space"``
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
      - ``"online"``, ``"partially_offline"``, ``"offline"``, ``"loading"``, or ``"unknown"``
      - ``"online"``
    * - ``updated_at``
      - string
      - ISO 8601-formatted timestamp of the last status update, or ``null`` if unknown
      - ``2024-06-27T09:30``

If the ``with_custom_properties`` query parameter is ``true``, the following additional attribute is included for each fixture.

.. list-table::
  :widths: 5 2 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``custom_properties``
    - object
    - Object properties and property values correspond to custom property names and values
    - ``{ "Custom Property 1": "value" }``

If the ``with_rdm_devices`` query parameter is ``true``, the following additional attribute is included for each fixture:

.. list-table::
  :widths: 5 2 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``rdm_devices``
    - array of objects
    - A list of RDM devices associated with this fixture
    - ``[ { "uid": "1234:56789abc" } ]``

Fixture
*******

GET
===

Get detailed information for a single fixture including its status.

``GET /api/fixtures/{fixtureNumber}``

Returns a JSON object with the same properties as contained in the :ref:`Fixtures Overview GET <fixtures-overview-http-get>` response.

Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format.rst
