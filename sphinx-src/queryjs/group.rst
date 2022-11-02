Group
#####

.. note:: Not applicable to |VLC|/|VLC+|

Functions
*********

master_intensity
================

``master_intensity(params, callback)``

Propagates to all controllers in a project.

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
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

For example:

.. code-block:: js

   // Master group 1 to 50% in 3 seconds
   Query.master_intensity({
     "num":1,
     "level":"50:100",
     "fade":3
   }, result => {
     // Check for error
   })

get_group_info
==============

Returns data about the fixture groups in the project.

``get_group_info(callback[, num])``

Returns an object with a single ``groups`` attribute, which has an array value. Each item in the array is a Group object with the same attributes as in the HTTP :ref:`group-http-get` response.

``num`` can be used to filter which groups are returned and is expected to be a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - string **or** integer
     - Define the numbers of the group that should be returned
     - ``"1,2,5-9"`` **or** ``5``

.. note:: Group 0 will return data about the *All Fixtures* group.

For example:

.. code-block:: js

   Query.get_group_info(g => {
     let name = g.groups[0].name // name of the first group returned
   }, {"num":"2-4"})
