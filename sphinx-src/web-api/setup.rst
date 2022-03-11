User Login
==========
.. note:: Expert only
  **TODO** is this true? Or will this also work on Designer?

HTTP
****

POST
====

Logs into a user accounts on the desired controller.

``POST /api/setup``

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``user``
     - string
     - The username
     - ``"admin"``
   * - ``password``
     - string
     - the user's password
     - ``"s3cur3Passw0rd"``


This can return the following:

- ``204``: OK
- ``400``: Bad Request
