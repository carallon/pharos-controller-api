Override
########

Functions
*********

set_group_override
==================

Set the Intensity, Red, Green, Blue levels for a group. Propagates to all controllers in a project.

``set_group_override(params, callback)``

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

clear_group_overrides
=====================

Release any overrides on a group, or all groups. Propagates to all controllers in a project.

``clear_group_overrides(params, callback)``

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
     - Optional. Group number. If not provided, all overrides are cleared.
     - ``1``
   * - ``fade``
     - float
     - Optional. Fade time in which to release overrides, in seconds.
     - ``2.0``

set_fixture_override
====================

Set the Intensity, Red, Green, Blue levels for a fixture. Propagates to all controllers in a project.

``set_fixture_override(params, callback)``

``params`` is expected to be an object with the same attributes as for `set_group_override`_.

clear_fixture_overrides
=======================

Release any overrides on a fixture, or all fixtures. Propagates to all controllers in a project.

``clear_fixture_overrides(params, callback)``

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
     - Optional. Fixture number. If not provided, all overrides are cleared.
     - ``1``
   * - ``fade``
     - float
     - Optional. Fade time in which to release overrides, in seconds.
     - ``2.0``

clear_all_overrides
===================

Release all overrides. Propagates to all controllers in a project.

``clear_all_overrides(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``fade``
     - float
     - Optional. Fade time in which to release overrides, in seconds.
     - ``2.0``
