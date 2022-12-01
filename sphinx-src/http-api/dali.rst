DALI
####

If the project uses DALI, the DALI API call can be used to get the status of connected DALI ballasts,
and to allow external systems to mark DALI issues as fixed.

Methods
*******

GET
===

Returns information about connected DALI devices on a particular interface - see :doc:`dali-interface` to retrieve a list of interfaces.

``GET /api/dali?interface=interface_num``

``interface_num`` is an integer referring to a specific interface.

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``online``
     - boolean
     - Whether or not the interface is currently online
   * - ``schedule``
     - object
     - A :doc:`objects/dali-schedule` object
   * - ``power``
     - object
     - A :doc:`objects/dali-power` object
   * - ``errors``
     - array of objects
     - An array of :doc:`objects/dali-error` objects
   * - ``ballast_status``
     - array of objects
     - An array of :doc:`objects/dali-ballast-status` objects


POST
====

Allows marking of a DALI error as fixed, or refresh of the DALI data.

``POST /api/dali``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``interface``
     - integer
     - The interface on which to perform the reset.
   * - ``address``
     - integer
     - The DALI short address on which to perform the reset.
   * - ``action``
     - string
     - Either ``mark_fixed`` or ``refresh``.
