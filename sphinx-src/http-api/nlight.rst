nLight
######

.. include:: snippets/endpoints-require-project.rst

The nLight API facilitates retrieval of live values from the nLight bus along with their mapped project targets and
triggers.

The ``address`` query parameter can be used on any of the following nLight endpoints to filter returned sub-devices. It
is expected to be either a single address or a string containing multiple comma-separated addresses, e.g., ``1`` or
``"1,3,16"``.


nLight Outputs
**************

GET
===

Read live data from nLight Outputs.

``GET /api/nlight/output``

Returns a JSON object with a single ``outputs`` attribute, which has an array value. Each item in the array is an nLight
Output object with the following attributes:

.. list-table::
  :widths: 5 2 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``address``
    - integer
    - Address of this nLight Output sub-device, from ``1``-``16``.
    - ``1``
  * - ``name``
    - string
    - User-assigned Output name.
    - ``"Output01"``
  * - ``level``
    - integer
    - Current level assigned to this Output, from ``1``-``1000``.
    - ``1000``

Project entities that are controlled by nLight Outputs are included by setting the ``with_targets`` query parameter to
``true``. An additional ``targets`` object attribute will be included with the following attributes:

.. list-table::
  :widths: 5 2 10
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
  * - ``intensity_masters``
    - array of objects
    - An array of :ref:`Intensity Master Mapping<nlight_mapping-intensity_master>` objects.
  * - ``scenes``
    - array of objects
    - An array of :ref:`Scene Mapping<nlight_mapping-scene>` objects.
  * - ``tag_sets``
    - array of objects
    - An array of :ref:`Tag Set Mapping<nlight_mapping-tag_set>` objects.


nLight Scenes
*************

GET
===

Read live data from nLight Scenes.

``GET /api/nlight/scene``

Returns a JSON object with a single ``scenes`` attribute, which has an array value. Each item in the array is an nLight
Scene object with the following attributes:

.. list-table::
  :widths: 5 2 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``address``
    - integer
    - Address of this nLight Scene sub-device, from ``1``-``16``.
    - ``1``
  * - ``name``
    - string
    - User-assigned Scene name.
    - ``"Scene01"``
  * - ``active``
    - boolean
    - Current active state of this Scene.
    - ``true``

Project entities that trigger nLight Scenes are included by setting the ``with_triggers`` query parameter to ``true``.
An additional ``triggers`` object attribute will be included with the following attributes:

.. list-table::
  :widths: 5 2 10
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
  * - ``scenes``
    - array of objects
    - An array of :ref:`Scene Mapping<nlight_mapping-scene>` objects.
  * - ``tags``
    - array of objects
    - An array of :ref:`Tags Mapping<nlight_mapping-tag>` objects.


nLight WallPods
***************

GET
===

Read live data from nLight WallPods.

``GET /api/nlight/wallpod``

Returns a JSON object with a single ``wallpods`` attribute, which has an array value. Each item in the array is an
nLight WallPod object with the following attributes:

.. list-table::
  :widths: 5 2 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``address``
    - integer
    - Address of this nLight WallPod sub-device, from ``1``-``16``.
    - ``1``
  * - ``name``
    - string
    - User-assigned WallPod name.
    - ``"Wallpod01"``
  * - ``level``
    - integer
    - Current level assigned to this WallPod, from ``1``-``100``.
    - ``100``
  * - ``status``
    - string
    - ``unpatched`` if the WallPod is not patched in the current project. Otherwise ``at_target_level``, ``near_target_level`` if within 5% of the target level, otherwise ``outside_target_level``.
    - ``at_target_level``


Project-nLight Mappings
***********************

.. _nlight_mapping-intensity_master:

Intensity Master
================

.. list-table::
  :widths: 4 3 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``level``
    - integer
    - Current level of this Intensity Master, from ``1`` - ``100``.
    - ``100``
  * - ``space``
    - string
    - The space this Intensity Master controls.
    - ``"7: Atrium"``

.. _nlight_mapping-scene:

Scene
=====

.. list-table::
  :widths: 4 3 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``scene``
    - string
    - Scene name.
    - ``"Scene 1"``
  * - ``space``
    - string
    - Name of the Scene's parent space.
    - ``"7: Atrium"``
  * - ``onstage``
    - boolean
    - Whether the Scene is currently affecting output of any fixtures.
    - ``true``

.. _nlight_mapping-tag:

Tags
====

.. list-table::
  :widths: 4 3 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``tag_set``
    - string
    - Tag Set name.
    - ``"1: Type of day"``
  * - ``tags``
    - array of strings
    - Names of mapped Tags.
    - ``["Non-working", "Working"]``
  * - ``active_tag``
    - string
    - The currently active Tag in the Tag Set.
    - ``"Off"``

.. _nlight_mapping-tag_set:

Tag Set
=======

.. list-table::
  :widths: 4 3 10 5
  :header-rows: 1

  * - Attribute
    - Value Type
    - Description
    - Value Example
  * - ``tag_set``
    - string
    - Tag Set name.
    - ``"2: nLight Output 1"``
  * - ``active_tag``
    - string
    - The currently active Tag in the Tag Set.
    - ``"Off"``
