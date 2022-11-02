Scene
#####

Functions
*********

start_scene
===========

``start_scene(params, callback)``

Propagates to all controllers in a project.

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
     - Scene number
     - ``5``

For ``callback`` please see `JavaScript Command Callback`_.

release_scene
=============

``release_scene(params, callback)``

Propagates to all controllers in a project.

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
     - Scene number
     - ``5``
   * - ``fade``
     - float
     - Optional. Release fade time in seconds. If not provided, the default fade time will be used.
     - ``2.0``

For ``callback`` please see `JavaScript Command Callback`_.

toggle_scene
============

``toggle_scene(params, callback)``

Propagates to all controllers in a project.

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
     - Scene number
     - ``5``
   * - ``fade``
     - float
     - Optional. The release fade time in seconds to apply if the toggle action results in the scene being released. If not provided, the default fade time will be used.
     - ``2.0``

For ``callback`` please see `JavaScript Command Callback`_.

release_all_scenes
==================

``release_all_scenes(params, callback)``

Propagates to all controllers in a project.

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
     - Optional. Release fade time in seconds. If not provided, the default fade time will be used.
     - ``2.0``
   * - ``group``
     - string
     - Optional. Scene group name: ``A``, ``B``, ``C`` or ``D``. Prepend the group name with ``!`` to apply the action to all groups *except* the specified group, e.g. ``!A``.
     - ``"B"``

For ``callback`` please see `JavaScript Command Callback`_.

release_all
===========

Release all timelines and scenes. Propagates to all controllers in a project.

``release_all(params, callback)``

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
     - Optional. Release fade time in seconds. If not provided, the default fade time will be used.
     - ``2.0``
   * - ``group``
     - string
     - Optional. Timeline/Scene group name: ``A``, ``B``, ``C`` or ``D``. Prepend the group name with ``!`` to apply the action to all groups *except* the specified group, e.g. ``!A``.
     - ``"B"``

For ``callback`` please see `JavaScript Command Callback`_.

get_scene_info
==============

Returns data about the scenes in the project and their state on the controller.

``get_scene_info(callback[, num])``

Returns an object with a single ``scenes`` attribute, which has an array value. Each item in the array is a Scene object with the same attributes as in the HTTP GET response.

``num`` can be used to filter which scenes are returned and is expected to be a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - string **or** integer
     - Define the numbers of the scene that should be returned
     - ``"1,2,5-9"`` **or** ``5``

For example:

.. code-block:: js

   Query.get_scene_info(s => {
     let name = s.scenes[0].name // name of the first scene returned
   }, {"num":"1,2-5"})


JavaScript Command Callback
***************************

.. include:: snippets/js-command-callback.rst
