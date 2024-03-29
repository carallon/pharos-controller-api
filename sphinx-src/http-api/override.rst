Override
########

Methods
*******

.. _override-http-put:

PUT
===

Set the Intensity, Red, Green, Blue levels for a |OVERRIDE_OPTIONS|.

.. only:: designer

  Action will propagate to all controllers in a project.

``PUT /api/override``

Payload is a JSON object with the following attributes:

.. only:: designer

  .. list-table::
    :widths: 4 3 10 4
    :header-rows: 1

    * - Attribute
      - Value Type
      - Description
      - Value Example
    * - ``target``
      - string
      - What the override should be applied to: ``group`` or ``fixture``
      - ``"group"``
    * - ``num``
      - integer
      - Optional. Group, fixture, or space number depending on ``target``. Group 0 means the *All Fixtures* group.
      - ``1``
    * - ``intensity``
      - integer or string
      - Optional. Either an integer (0-255) representing the intensity to set as part of override **or** the string ``"snapshot"`` to capture the current intensity of the fixture(s) and set this as the override value. Intensity override will not be changed if this attribute isn't provided.
      - ``128``
    * - ``colour``
      - `Override Colour`_ or string
      - Optional. Specifies the colour to set as part of the override. Either an `Override Colour`_ or the string ``"snapshot"`` to capture the current colour of the fixture(s) and set this as the override.
      -
    * - ``temperature``
      - integer or string
      - Optional. Either an integer (0-255) representing the temperature component to set as part of override **or** the string ``"snapshot"`` to capture the current temperature component of the fixture(s) and set this as the override value. Temperature override will not be changed if this attribute isn't provided.
      - ``128``
    * - ``fade``
      - float
      - Optional. Fade time to apply the override change, in seconds.
      - ``2.0``
    * - ``path``
      - string
      - Optional. Crossfade path to use when applying the override: ``Default``, ``Linear``, ``Start``, ``End``, ``Braked``, ``Accelerated``, ``Damped``, ``Overshoot``, ``Col At Start``, ``Col At End``, ``Int At Start``, ``Int At End``, ``Colour First``, ``Intensity First``
      - ``"Braked"``

.. only:: expert

  .. list-table::
    :widths: 4 3 10 4
    :header-rows: 1

    * - Attribute
      - Value Type
      - Description
      - Value Example
    * - ``target``
      - string
      - What the override should be applied to. ``fixture`` or ``space``
      - ``"fixture"``
    * - ``num``
      - integer
      - Fixture number.
      - ``1``
    * - ``intensity``
      - integer or string
      - Optional. Either an integer (0-255) representing the intensity to set as part of override **or** the string ``"snapshot"`` to capture the current intensity of the fixture(s) and set this as the override value. Intensity override will not be changed if this attribute isn't provided.
      - ``128``
    * - ``colour``
      - `Override Colour`_ or string
      - Optional. Specifies the colour to set as part of the override. Either an `Override Colour`_ or the string ``"snapshot"`` to capture the current colour of the fixture(s) and set this as the override.
      -
    * - ``temperature``
      - integer or string
      - Optional. Either an integer (0-255) representing the temperature component to set as part of override **or** the string ``"snapshot"`` to capture the current temperature component of the fixture(s) and set this as the override value. Temperature override will not be changed if this attribute isn't provided.
      - ``128``
    * - ``fade``
      - float
      - Optional. Fade time to apply the override change, in seconds.
      - ``2.0``
    * - ``path``
      - string
      - Optional. Crossfade path to use when applying the override: ``Default``, ``Linear``, ``Start``, ``End``, ``Braked``, ``Accelerated``, ``Damped``, ``Overshoot``, ``Col At Start``, ``Col At End``, ``Int At Start``, ``Int At End``, ``Colour First``, ``Intensity First``
      - ``"Braked"``

.. _override-colour-json:

Override Colour
---------------

The value of the ``colour`` attribute in a PUT override request is a JSON object, specifying colour as *either* `RGB`_ or `Hue/Saturation`_ values.

RGB
^^^

Colour as RGB for ``colour`` in an override :ref:`override-http-put` request:

.. list-table::
   :widths: 4 3 10 3
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``red``
     - integer or string
     - Optional. Red component to set as part of override: 0-255, or a percentage (0-100) followed by the % sign. Red override will not be changed if this attribute isn't provided.
     - ``255``
   * - ``green``
     - integer or string
     - Optional. Green component to set as part of override: 0-255, or a percentage (0-100) followed by the % sign. Green override will not be changed if this attribute isn't provided.
     - ``255``
   * - ``blue``
     - integer or string
     - Optional. Blue component to set as part of override: 0-255, or a percentage (0-100) followed by the % sign. Blue override will not be changed if this attribute isn't provided.
     - ``255``

Hue/Saturation
^^^^^^^^^^^^^^

Colour as hue/saturation for ``colour`` in an override :ref:`override-http-put` request:

.. list-table::
   :widths: 4 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``hue``
     - integer
     - Hue component to set as part of override: 0-255.
     - ``0``
   * - ``saturation``
     - integer
     - Saturation component to set as part of override: 0-255.
     - ``255``

.. note::

   Both ``hue`` and ``saturation`` are required for the request to be valid.


.. only:: designer

  Example Overrides
  ^^^^^^^^^^^^^^^^^

  Override group 1 to full intensity, using 0-255 values, and set colour to yellow:

  .. code-block:: json

    {
        "target": "group",
        "num": "1",
        "intensity": 255,
        "colour": {
            "red": 255,
            "green": 255,
            "blue": 0
        }
    }

  Override fixture 1 to 50% intensity and green, using percentages:

  .. code-block:: json

    {
        "target": "fixture",
        "num": 1,
        "intensity": "50%",
        "colour": {
            "red": "0%",
            "green": "100%",
            "blue": "0%"
        }
    }

  Override fixture 2 to 80% intensity and blue, using hue and saturation:

  .. code-block:: json

    {
        "target": "fixture",
        "num": 2,
        "intensity": "50%",
        "colour": {
            "hue": 200,
            "saturation": 240
        }
    }

  Override group 3 colour temperature of 44 with a fade time of 5 seconds:

  .. code-block:: json

    {
        "target": "group",
        "num": 3,
        "intensity": 255,
        "temperature": 44,
        "fade": 5.0
    }

  Snapshot the colour and intensity of all fixtures:

  .. code-block:: json

    {
        "target": "group",
        "num": "0",
        "intensity": "snapshot",
        "colour": "snapshot"
    }

DELETE
======

Release any overrides on |OVERRIDE_OPTIONS|.

.. only:: designer

  Action will propagate to all controllers in a project.

``DELETE /api/override``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 4 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``target``
     - string
     - What the overrides should be cleared on: |OVERRIDE_OPTIONS|.
     - ``"fixture"``
   * - ``num``
     - integer
     - Optional. |OVERRIDE_OPTIONS| number, depending on ``target``. If not provided, ``target`` is ignored and all overrides are cleared.
     - ``1``
   * - ``fade``
     - float
     - Optional. Fade time in which to release overrides, in seconds.
     - ``2.0``
