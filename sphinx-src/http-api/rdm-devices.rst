.. _rdm-devices:

RDM Devices
###########

All properties described below relating to an RDM device's status are obtained by the :ref:`status-monitor`.

RDM Devices Overview
********************

.. _rdm-devices-overview-http-get:

GET
===

Get an overview of RDM devices including their statuses.

``GET /api/rdm_devices[?fixture=fixtureNumber][&unpatched=true]``

``fixture`` can be used the filter the response to devices patched to a single fixture. Set ``unpatched`` to ``true`` to return only unpatched devices.

One of ``fixture`` or ``unpatched`` is required and may not be provided together.

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
     - Combined universe key and address (see `Universe Key String Format`_). Only included if ``status`` is ``online``.
     - ``"dmx:2:101"``
   * - ``rdm``
     - object
     - RDM parameters cached from the latest status monitor run. Only included if ``status`` is ``online``.
     - ``{}``
   * - ``status``
     - string
     - ``"online"``, ``"offline"``, ``"loading"``, or ``"unknown"``
     - ``"online"``
   * - ``updated_at``
     - string
     - ISO 8601-formatted timestamp of the last status update, or ``null`` if unknown
     - ``2024-06-27T09:30``

RDM Device
**********

GET
===

Get a single RDM device including its status.

``GET /api/rdm_devices/{deviceId}``

Returns a JSON object with the same properties as contained in the :ref:`RDM Devices Overview GET <rdm-devices-overview-http-get>` response.

Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format.rst
