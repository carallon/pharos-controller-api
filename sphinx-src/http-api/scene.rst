Scene
#####

Methods
*******

POST
====

Control a scene in the project. Action will propagate to all controllers in a project.

``POST /api/scene``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
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
   :widths: 5 2 10 5
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
