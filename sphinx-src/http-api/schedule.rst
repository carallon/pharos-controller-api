Schedule
########

Methods
*******

GET
===

Get whether the controller schedule is enabled or disabled.

When the schedule is disabled, no configured scheduled events occur. This state lasts until it is re-enabled, or the controller is reset.

``GET /api/schedule``

Returns a JSON object with a single attribute, ``enable``, which is true if the schedule is enabled, false if it is disabled.

PUT
===

Set whether the controller schedule is enabled or disabled.

``PUT /api/schedule``

Supply a JSON object with a single ``enable`` attribute, true if the schedule is to be enabled, false if it is to be disabled.
