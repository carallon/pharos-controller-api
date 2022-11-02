Group
#####

.. note:: Not applicable to |VLC|/|VLC+|

Methods
*******

POST
====

Control a group; currently the only supported action is to master the intensity of a group (applied as a multiplier to output levels). Action will propagate to all controllers in a project.

``POST /api/group``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``action``
     - string
     - The action to perform on the group. Currently only ``master_intensity`` is supported.
     - ``"master_intensity"``
   * - ``num``
     - integer
     - Group number. Group 0 means the *All Fixtures* group.
     - ``1``
   * - ``level``
     - float or string containing a bounded integer
     - Master level to set on the group
     - ``0.5 or "50:100"``
   * - ``fade``
     - float
     - Optional. Fade time to apply the intensity change, in seconds.
     - ``2.0``
   * - ``delay``
     - float
     - Optional. Time to wait before applying the intensity change, in seconds.
     - ``2.0``

.. _group-http-get:

GET
===

Returns data about the fixture groups in the project.

``GET /api/group[?num=groupNumbers]``

``num`` can be used to filter which groups are returned and is expected to be either a single number or a string expressing the required groups, e.g. ``"1,2,5-9"``.

.. note:: Group 0 will return data about the *All Fixtures* group.

Returns a JSON object with a single ``groups`` attribute, which has an array value. Each item in the array is a Group object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Group number (only included for user-created groups)
     - ``1``
   * - ``name``
     - string
     - Group name
     - ``"Group 1"``
   * - ``level``
     - integer
     - Group master level, 0-100
     - ``100``
