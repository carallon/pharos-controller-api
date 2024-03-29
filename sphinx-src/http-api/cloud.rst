Cloud
#####

Methods
*******

GET
===

Returns the state of connectivity to the remote site.

``GET /api/cloud``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``connected``
     - boolean
     - Whether or not the system is currently connected to the remote site
   * - ``connecting``
     - boolean
     - Whether or not the system is currently in the process of connecting to the remote site


POST
====

Allows configuration of the parameters for connection to the remote site.

``POST /api/cloud``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``action``
     - string
     - Either ``set_device_key`` or  ``clear_device_key``
   * - ``cloud_device_key``
     - string
     - Only required for ``set_device_key`` - the string to set as the key.
