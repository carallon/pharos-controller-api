DALI Interface
##############

The DALI Interface API allows retrieval of a list of DALI interfaces in the system.

Methods
*******

GET
===

Returns an array of DALI interfaces

``GET /api/dali_interface``

Returns an array of JSON objects with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``id``
     - integer
     - The ID of the interface
   * - ``name``
     - string
     - The assigned string name of the interface
