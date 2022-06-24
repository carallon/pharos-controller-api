Scene
#####

HTTP
****

POST
====

Control a scene in the project.

``POST /api/scene``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``action``
     - string
     - The action to perform on the scene(s): ``start``, ``release``, ``toggle``
     - ``"start"``
   * - ``num``
     - integer
     - The number of the scene to perform the action on. If not present, the action will be applied to all scenes in the project; omitting this attribute is valid for ``release``.
     - ``1``
   * - ``fade``
     - number
     - Optional. The fade time to apply to a ``release`` action, in seconds, or the scene release that results from a ``toggle`` action. If not provided, the default release fade time will be used.
     - ``2.0``
   * - ``group``
     - string
     - Optional. Scene group name: ``A``, ``B``, ``C`` or ``D``. Prepend the group name with ``!`` to apply the action to all groups *except* the specified group, e.g. ``!A``. This attribute is valid for a ``release`` action without a specified ``num``, meaning *release all scenes*.
     - ``"B"``

For example, to start a scene 2, the request payload is:

.. code-block:: json

   {
     "action": "start",
     "num": 2
   }

To release scene 2 in 3.5 seconds, the request payload would be:

.. code-block:: json

   {
     "action": "release",
     "num": 2,
     "fade": 3.5
   }

To toggle scene 2, and release it in 2 seconds if it's already been started, the request payload would be:

.. code-block:: json

   {
     "action": "toggle",
     "num": 2,
     "fade": 2.0
   }

To release all scenes in 2 seconds, the request payload would be:

.. code-block:: json

   {
     "action": "release",
     "fade": 2.0
   }

To release all scenes except those in group B in 2 seconds, the request payload would be:

.. code-block:: json

   {
     "action": "release",
     "group": "!B",
     "fade": 2.0
   }


GET
===

Returns data about the scenes in the project and their state on the controller.

``GET /api/scene[?num=sceneNumbers]``

``num`` can be used to filter which scenes are returned and is expected to be either a single number or a string expressing the required scenes, e.g. ``"1,2,5-9"``.

Returns a JSON object with a single ``scenes`` attribute, which has an array value. Each item in the array is a Scene object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Scene number
     - ``1``
   * - ``name``
     - string
     - Scene name
     - ``"Scene 1"``
   * - ``state``
     - string
     - ``none``, ``started``
     - ``"none"``
   * - ``onstage``
     - boolean
     - Whether the scene is affecting output of any fixtures
     - ``true``

JavaScript
**********

start_scene
===========

``start_scene(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
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

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
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

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
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

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
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

Release all timelines and scenes.

``release_all(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
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
   :widths: 2 2 10 5
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

.. include:: ../snippets/js-command-callback.rst
