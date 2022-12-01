DALI Ballast Status
###################

The DALI ballast status object has the following attributes:

.. list-table::
   :widths: 5 2 10 4
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``address``
     - integer
     - The ballast address
     - ``12``
   * - ``user_name``
     - string
     - The user assigned name of the ballast
     - ``"Center Room"``
   * - ``status``
     - string
     - A string representing the current status of the ballast
     - ``"Lamp Failure"``
   * - ``actual_level``
     - integer
     - The current actual output level of the ballast
     - ``128``
   * - ``battery_level``
     - integer
     - For emergency ballasts only - the level of the battery reported
     - ``12``
   * - ``battery_charged``
     - boolean
     - Whether or not the battery is charged
     - ``True``
   * - ``lamp_emergency_hours``
     - integer
     - How many hours the fixture has been on in emergency state
     - ``12``
   * - ``lamp_total_hours``
     - integer
     - How many hours the fixture has been on in total
     - ``400``
   * - ``last_status_check``
     - date/time
     - The last date and time the ballast status was checked
     - ``0``
