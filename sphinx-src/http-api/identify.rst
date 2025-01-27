Identify
########

Methods
*******

POST
====

Toggle identify mode on the controller.

``POST /api/identify``

In identify mode, the controller will flash its blue "Identify" LED continuously.

PUT
===

Enable or disable identify mode on the controller.

``PUT /api/identify``

This endpoint accepts a JSON object with a single boolean ``enable`` property.
