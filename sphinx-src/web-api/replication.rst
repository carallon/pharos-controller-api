Replication
###########

Returns data about the install replication.

HTTP
****

GET
===

``GET /api/replication``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Value Example
   * - ``name``
     - string
     - ``"Help Project"``
   * - ``unique_id``
     - string
     - ``"{6b48627a-1d5e-4b2f-81e2-481e092a6a79}"``

JavaScript
**********

get_replication
===============

``get_replication(callback)``

Returns an object with the same attributes as in the HTTP GET response.
