Beacon
######

Methods
*******

POST
====

Toggle beacon mode on the controller.

``POST /api/beacon``

.. only:: express

    In beacon mode, a controller will flash its LEDs continuously.

.. only:: designer

    In beacon mode, a controller will flash its LEDs or its screen continuously.

PUT
===

Enable or disable beacon mode on the controller.

``PUT /api/beacon``

This endpoint accepts a JSON object with a single boolean ``enable`` property.
