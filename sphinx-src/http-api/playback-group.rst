Playback Group
##############

Methods
*******

.. only:: designer

  GET
  ===

  Returns data about the playback groups in the project on the controller.

  ``GET /api/playback_group[?num=playbackGroupNumbers]``

  ``num`` can be used to filter which scenes are returned and is expected to be either a single number or a string expressing the required playback groups, e.g. ``"1,2,5-9"``.

  Returns a JSON object with a single ``playback_groups`` attribute, which has an array value. Each item in the array is a Playback group object with the following attributes:

  .. list-table::
    :widths: 3 3 10 5
    :header-rows: 1

    * - Attribute
      - Value Type
      - Description
      - Value Example
    * - ``num``
      - integer
      - Playback Group number
      - ``1``
    * - ``name``
      - string
      - Playback Group name
      - ``"Back of House"``
