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

``GET /api/rdm_devices[?fixture=fixtureNumber][&offline=true][&unpatched=true]``

``fixture`` can be used the filter the response to devices patched to a single fixture. Set ``offline`` to ``true`` to return only offline devices, or set ``unpatched`` to ``true`` to return only unpatched devices.

One of ``fixture``, ``offline``, or ``unpatched`` is required, and no two parameters may be provided together.

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
   * - ``fixture_number``
     - number
     - User number of the fixture this device is assigned to, or ``null`` if not patched.
     - ``123``
   * - ``issues``
     - array of objects
     - Issues found with this RDM device. See `Device Issues`_.
     - ``[{"issue":"address_mismatch","valid":[1,11,51]}]``
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
   * - ``variant_key``
     - string
     - A unique identifier for the RDM device variant. See `Device Variant String Format`_.
     - ``"25972-517-17170449"``

RDM Device
**********

GET
===

Get a single RDM device including its status.

``GET /api/rdm_devices/{deviceId}``

Returns a JSON object with the same properties as contained in the :ref:`RDM Devices Overview GET <rdm-devices-overview-http-get>` response.

.. only:: not expert

  PUT
  ===

  Patch an unpatched RDM device.

  ``PUT /api/rdm_devices/{deviceId}/patch``

  The payload is a JSON object with the following attributes:

  .. list-table::
    :widths: 4 3 10 5
    :header-rows: 1

    * - Attribute
      - Value Type
      - Description
      - Value Example
    * - ``action``
      - string
      - The patch action to perform.
      - ``"assign", or "replace"``

  Assign
  ------

  Assign a new RDM device to a fixture. When ``action`` is ``assign``, the following additional attributes are required:

  .. list-table::
    :widths: 4 3 10 5
    :header-rows: 1

    * - Attribute
      - Value Type
      - Description
      - Value Example
    * - ``fixture_number``
      - number
      - User number of the fixture this RDM device will be assigned to.
      - ``123``

  Replace
  -------

  Replace an offline RDM device. When ``action`` is ``replace``, the following additional attributes are required:

  .. list-table::
    :widths: 4 3 10 5
    :header-rows: 1

    * - Attribute
      - Value Type
      - Description
      - Value Example
    * - ``target_device_id``
      - string
      - The RDM UID of the device to replace.
      - ``"1234:56789abc"``

Device Issues
*************

.. _rdm-devices-device-issues:

The status monitor tracks patch issues for each patched RDM device. The following issues are detected, discriminated by the ``issue`` field:

Address Mismatch
================

The DMX start address of the RDM device does not match any patched addresses for the parent fixture on the universe upon which it was discovered.

.. list-table::
  :widths: 4 3 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``issue``
    - string
    - Issue type discriminator.
    - ``"address_mismatch"``
  * - ``valid``
    - array of integers
    - Valid DMX start addresses for this device on the current universe.
    - ``[1,11,51]``

Output Mismatch
===============

The RDM device was discovered on an output upon which the parent fixture is not patched.

.. list-table::
  :widths: 4 3 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``issue``
    - string
    - Issue type discriminator.
    - ``"output_mismatch"``
  * - ``valid``
    - array of strings
    - Valid outputs for this device. See `Universe Key String Format`_.
    - ``["dmx:1:1","riog4:1:2"]``

Device Variant String Format
****************************

.. include:: ../snippets/rdm-device-variant-key-string-format.rst

Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format.rst
