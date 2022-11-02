Content Targets
###############

.. note:: |VLC|/|VLC+| only

Methods
*******

POST
====

Control a content target; currently the only supported action is to master the intensity of a content target (applied as a multiplier to output levels).

``POST /api/content_target``

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
     - The action to perform on the content target. Currently only ``master_intensity`` is supported.
     - ``"master_intensity"``
   * - ``type``
     - string
     - Optional. Type of content target (only relevant on |VLC+|): ``primary``, ``secondary``, ``target_3``, ``target_4``, ``target_5``, ``target_6``, ``target_7``, ``target_8``. Defaults to ``primary``.
     - ``"secondary"``
   * - ``level``
     - float or string containing a bounded integer
     - Master intensity level to set on the content target
     - ``0.5 or "50:100"``
   * - ``fade``
     - float
     - Optional. Fade time to apply the intensity change, in seconds.
     - ``2.0``
   * - ``delay``
     - float
     - Optional. Time to wait before applying the intensity change, in seconds.
     - ``2.0``

.. _content-target-http-get:

GET
===

Returns information about the current state of all Content Targets in the project.

``GET /api/content_target``

Returns a JSON object with a single ``content_targets`` attribute, which has an array value. Each item in the array is a Content Target object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - Content target name
     - ``"Primary"``
   * - ``level``
     - integer
     - Current intensity master level of the content target, 0-100
     - ``100``
