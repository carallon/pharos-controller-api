Project
#######

Returns data about the current project.

HTTP
****

GET
===

``GET /api/project``

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
   * - ``author``
     - string
     - ``"Pharos"``
   * - ``filename``
     - string
     - ``"help_project_v1.pd2"``
   * - ``unique_id``
     - string
     - ``"{6b48627a-1d5e-4b2f-81e2-481e092a6a79}"``
   * - ``upload_date``
     - string
     - ``"2017-01-30T15:19:08"``

JavaScript
**********

get_project_info
================

``get_project_info(callback)``

Returns an object with the same attributes as in the HTTP GET response.

For example:

.. code-block:: js

   Query.get_project_info(project => {
     const author = project.author
   })