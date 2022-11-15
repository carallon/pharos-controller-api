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
     - Optional. Group name: ``A``, ``B``, ``C`` or ``D``. Prepend the group name with ``!`` to apply the action to all groups *except* the specified group, e.g. ``!A``.
     - ``"B"``
