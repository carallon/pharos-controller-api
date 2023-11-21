.. note::
  You can provide:
    * No arguments - this will release all with the default fade time.
    * A fade time, which will be used to release all.
    * Or, both a fade time and a group.

.. list-table::
   :widths: 3 3 10 2
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``fade``
     - float
     - Optional. Release fade time in seconds. If not provided, the default fade time will be used.
     - ``2.0``
   * - ``group``
     - string
     - Optional. Group name: ``A`` through ``H``. Prepend the group name with ``!`` to apply the action to all groups *except* the specified group, e.g. ``!A``.
     - ``"B"``
