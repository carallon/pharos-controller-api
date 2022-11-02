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
     - Scene group name (``A``, ``B``, ``C``, ``D`` or empty string)
     - ``"A"``
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
