DateTime
########

A ``DateTime`` object is returned from e.g. :doc:`system` properties.

``DateTime`` can only represent time points on or after 2000/01/01 00:00 UTC.

Methods
*******

DateTime.new(epoch) -> DateTime
===============================

Create a new DateTime from the number of seconds since 1970/01/01 00:00 UTC, a.k.a ``epoch``.

Returns nil if the ``epoch`` is invalid.

DateTime.new(year, month, monthDay) -> DateTime
===============================================

Create a new DateTime from a ``year`` (4 digits, i.e. ``2000``), ``month`` (1-12), ``monthDay`` (1-30).

Returns nil if the date is invalid. For example 2023/02/29 (2023 was NOT a leap year).

DateTime.new(year, month, monthDay, hour, minute, second) -> DateTime
=====================================================================

Create a new DateTime from a ``year`` (4 digits, i.e. ``2000``), ``month`` (1-12), ``monthDay`` (1-30), ``hour`` (0-23), ``minute`` (0-59), ``second`` [Optional] (0-59).

The time is expected to be in local time.

Returns nil if the time point is invalid. For example 2023/02/29 (2023 was NOT a leap year), or 12:60:00.

Properties
**********

.. list-table::
   :widths: 3 5 3
   :header-rows: 1

   * - Property
     - Value Type
     - Value Example
   * - ``year``
     - integer
     - ``2022``
   * - ``month``
     - integer
     - ``12``
   * - ``monthday``
     - integer
     - ``3``
   * - ``time_string``
     - string
     - ``"11:35:32"``
   * - ``date_string``
     - string
     - ``"03 Dec 2022"``
   * - ``weekday``
     - integer (0 => Sunday)
     - ``0``
   * - ``hour``
     - integer
     - ``11``
   * - ``minute``
     - integer
     - ``35``
   * - ``second``
     - integer
     - ``32``
   * - ``utc_timestamp``
     - integer
     - ``1670045912``
