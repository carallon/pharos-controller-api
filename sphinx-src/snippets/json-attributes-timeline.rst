.. list-table::
   :widths: 3 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``1``
   * - ``state``
     - string
     - The new state of the timeline: ``none``, ``running``, ``paused``, ``holding_at_end``, ``released``
     - ``"running"``
   * - ``onstage``
     - boolean
     - Whether the timeline is currently affecting the output of any fixtures in the project.
     - ``true``
   * - ``position``
     - integer
     - Current time position of the timeline playback, in milliseconds
     - ``5000``
