Fixture
#######

A ``Fixture`` object is returned from :ref:`Lua_get_fixture`.

Properties
**********

.. list-table::
   :widths: 5 3 7 4
   :header-rows: 1

   * - Property
     - Value Type
     - Description
     - Value Example
   * - ``groups``
     - Table of :doc:`group` objects
     - A list of the groups containing this fixture
     -
   * - ``issues``
     - Table of issues
        .. include:: enum/fixture-issue.rst
     - A list of issues affecting this fixture
     - ``{ISSUE_ADDRESS_MISMATCH}``
   * - ``manufacturer``
     - string
     - Manufacturer name of the fixture
     - ``"Example Manufacturer"``
   * - ``name``
     - string
     - Fixture name
     - ``"Downlight"``
   * - ``number``
     - integer
     - User number
     - ``1``
   * - ``patch``
     - Table of :doc:`patch-point` objects
     - Patch points assigned to this fixture
     -
   * - ``protocol``
     -
        .. include:: enum/fixture-protocol.rst
     - The output protocol used by this fixture
     - ``PROTOCOL_DMX``
   * - ``status``
     -
        .. include:: enum/fixture-status.rst
     - The status of this fixture
     - ``STATUS_ONLINE``
   * - ``type``
     - string
     - Fixture type from the fixture library
     - ``LED - RGBW 8 bit``
   * - ``updated_at``
     - :doc:`date-time` or ``nil``
     - The last status update for this fixture or nil if there has been no update
     -
   * - ``custom_properties``
     - table of strings
     - The custom properties for this fixture as configured in Designer
     - ``{"Location" = "Room 1"}``
   * - ``rdm_devices``
     - table of `RDM DeviceId <RDM_DEVICE_ID_>`_
     - RDM UIDs associated with this fixture - empty if fixture has no RDM devices associated (e.g. a DALI fixture)
     -

.. _RDM_DEVICE_ID: https://pharos-io-module-developer-guide.readthedocs.io/en/latest/api/rdm/device-id.html

For example:

.. include:: code-examples/fixture.rst
