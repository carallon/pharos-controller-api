User
####

This allows user accounts on the controller to be added, modified, or removed.

Methods
*******

POST
====

``POST /api/user``

Add a new user. The payload is a JSON object with the following attributes:

.. list-table::
   :widths: 4 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``session_password``
     - string
     - The password for the current session.
     - ``"my_password"``
   * - ``username``
     - string
     - The name of the new user to add
     - ``"bob"``
   * - ``password``
     - string
     - The new user's password.
     - ``"bobs_password"``
   * - ``access``
     - array of strings
     - The access level(s) to grant the new user. Includes Admin, Control and Status.
     - ``["Control", "Status"]``

PUT
===

``PUT /api/user``

Update a user account with a new password and/or access groups. The payload is a JSON object with the following attributes:

.. list-table::
   :widths: 4 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``session_password``
     - string
     - The password for the current session.
     - ``"my_password"``
   * - ``"username"``
     - string
     - The name of the user to modify
     - ``"bob"``
   * - ``password``
     - string
     - The user's updated password.
     - ``"bobs_password"``
   * - ``access``
     - array of strings
     - The access level(s) to grant the user. Includes Admin, Control and Status.
     - ``["Control", "Status"]``

DELETE
======

``DELETE /api/user``

Update a user account with a new password and/or access groups. The payload is a JSON object with the following attributes:

.. list-table::
   :widths: 4 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``session_password``
     - string
     - The password for the current session.
     - ``"my_password"``
   * - ``username``
     - string
     - The name of the user to delete
     - ``"bob"``
