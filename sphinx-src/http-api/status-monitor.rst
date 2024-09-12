.. _status-monitor:

Status Monitor
##############

  These endpoints are not available on VLC or VLC+.

Status monitor results are accessed through the :ref:`fixtures` and :ref:`rdm-devices` endpoints.

Methods
*******

GET
===

Returns an overview of the status monitor.

``GET /api/status_monitor``

Returns a JSON object containing a single ``latest_refresh_all`` attribute with the following attributes:

.. list-table::
   :widths: 3 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``completed_at``
     - string
     - ISO 8601-formatted timestamp of the latest full refresh
     - ``"2024-06-27T09:30"``
   * - ``discovered_device_count``
     - integer
     - Total discovered device count including both patched and unpatched devices
     - ``50``
   * - ``unpatched_device_count``
     - integer
     - Unpatched device count
     - ``3``

The ``latest_refresh_all`` attribute will be ``null`` if a full status monitor refresh has not been performed since boot.

POST
====

Control the status monitor. Currently the only supported action is to refresh devices.

``POST /api/status_monitor``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 3 4 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``action``
     - string
     - The action to perform on the status monitor. Currently only ``refresh`` is supported.
     - ``"refresh"``
   * - ``fixture_number``
     - integer
     - User number of the fixture to refresh. Omit to refresh all fixtures and devices.
     - ``1``
