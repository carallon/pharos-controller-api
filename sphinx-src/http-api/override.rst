Override
########

Methods
*******

PUT
===

Set the Intensity, Red, Green, Blue levels for a fixture or group. Action will propagate to all controllers in a project.

``PUT /api/override``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``target``
     - string
     - What the override should be applied to: ``group``, ``fixture``.
     - ``"group"``
   * - ``num``
     - integer
     - Group or fixture number, depending on ``target``. Group 0 means the *All Fixtures* group.
     - ``1``
   * - ``intensity``
     - integer
     - Optional. Intensity to set as part of override: 0-255. Intensity override will not be changed if this attribute isn't provided.
     - ``128``
   * - ``red``
     - integer
     - Optional. Red component to set as part of override: 0-255. Red override will not be changed if this attribute isn't provided.
     - ``255``
   * - ``green``
     - integer
     - Optional. Green component to set as part of override: 0-255. Green override will not be changed if this attribute isn't provided.
     - ``255``
   * - ``blue``
     - integer
     - Optional. Blue component to set as part of override: 0-255. Blue override will not be changed if this attribute isn't provided.
     - ``255``
   * - ``temperature``
     - integer
     - Optional. Temperature component to set as part of override: 0-255. Temperature override will not be changed if this attribute isn't provided.
     - ``128``
   * - ``fade``
     - float
     - Optional. Fade time to apply the override change, in seconds.
     - ``2.0``
   * - ``path``
     - string
     - Optional. Crossfade path to use when applying the override: ``Default``, ``Linear``, ``Start``, ``End``, ``Braked``, ``Accelerated``, ``Damped``, ``Overshoot``, ``Col At Start``, ``Col At End``, ``Int At Start``, ``Int At End``, ``Colour First``, ``Intensity First``
     - ``"Braked"``

DELETE
======

Release any overrides on fixtures or groups. Action will propagate to all controllers in a project.

``DELETE /api/override``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``target``
     - string
     - What the overrides should be cleared on: ``group``, ``fixture``.
     - ``"group"``
   * - ``num``
     - integer
     - Optional. Group or fixture number, depending on ``target``. If not provided, ``target`` is ignored and all overrides are cleared.
     - ``1``
   * - ``fade``
     - float
     - Optional. Fade time in which to release overrides, in seconds.
     - ``2.0``
