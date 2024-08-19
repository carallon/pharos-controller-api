.. _status-monitor:

Status Monitor
##############

  These endpoints are not available on VLC or VLC+.

Status monitor results are accessed through the :ref:`fixtures` and :ref:`rdm-devices` endpoints.

Methods
*******

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
