Scene
#####

A ``Scene`` object is returned from :ref:`Lua_get_scene`.

Properties
**********

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Property
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - Scene name
     - ``"Scene 1"``
   * - ``group``
     - string
     - Scene group name
     - ``"Group 1"``
   * - ``state``
     - integer
     - Integer value of constants: ``Scene.NONE``, ``Scene.STARTED`` or ``Scene.RELEASED``
     - ``1``
   * - ``onstage``
     - boolean
     - Whether the scene is affecting output of any fixtures
     - ``false``
   * - ``custom_properties``
     - table
     - Table keys and values correspond to custom property names and values
     -

For example:

.. include:: code-examples/scene.rst

Member functions
****************

The following are member functions of ``Scene`` objects.

.. _Lua_scene_start:

start
=====

``start()``

Starts the scene. For example:

.. code-block:: lua

   -- start scene 1
   get_scene(1):start()


.. _Lua_scene_start_release_others:

start_release_others
====================

``start_release_others(group[, fade[, same_group]])``

Starts the scene and releases others.

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``group``
     - string **or** integer
     - Optional scene group name or number.  If name, prepend the name with ``!`` to apply the action to all scenes *except* those in the specified group. Omit to apply the action to all scenes.
     - ``"Group 1"``, ``"!Group 2"`` or ``3``
   * - ``fade``
     - float
     - Optional fade time to use when releasing other scenes, in seconds
     - ``2.0``
   * - ``same_group``
     - boolean
     - Optional flag to target the same group as the selected timeline. This flag has no effect when ``group`` is set.
     - ``true``

For example:

.. code-block:: lua

   -- start scene 1 and release all others in the default time
   get_scene(1):start_release_others()
   -- start scene 1 and release others except those in group B in 2 seconds
   get_scene(1):start_release_others('!B', 2.0)
   -- start scene 1 and release others in the same group in the default time
   get_scene(1):start_release_others(nil, nil, true)


.. _Lua_scene_release:

release
=======

``release([fade])``

Releases the scene. Optionally specify a ``fade`` time in seconds as a float, e.g. ``2.0``.

For example:

.. code-block:: lua

   -- release scene 3 with a fade of 1 second
   get_scene(3):release(1.0)


.. _Lua_scene_toggle:

toggle
======

``toggle([fade])``

Toggles the playback of the scene - if it's running, release it; if it's not running, start it. Optionally specify a release ``fade`` time in seconds as a float, e.g. ``2.0``.

For example:

.. code-block:: lua

   -- toggle scene 2, releasing in time 3 secs if it's running
   get_scene(2):release(3.0)
