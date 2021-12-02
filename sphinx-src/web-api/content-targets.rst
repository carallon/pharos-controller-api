Content Targets
###############

.. note:: VLC/VLC+ only

HTTP
****

POST
====

Control a content target; currently the only supported action is to master the intensity of a content target (applied as a multiplier to output levels).

``POST /api/content_target``

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
     - The action to perform on the content target. Currently only ``master_intensity`` is supported.
     - ``"master_intensity"``
   * - ``type``
     - string
     - Optional. Type of content target (only relevant on VLC+): ``primary``, ``secondary``, ``target_3``, ``target_4``, ``target_5``, ``target_6``, ``target_7``, ``target_8``. Defaults to ``primary``.
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
   :widths: 2 2 10 5
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

JavaScript
**********

master_content_target_intensity
===============================

``master_content_target_intensity(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``type``
     - string
     - Optional. Type of content target (only relevant on VLC+): ``primary``, ``secondary``, ``target_3``, ``target_4``, ``target_5``, ``target_6``, ``target_7``, ``target_8``. Defaults to ``primary``.
     - ``"secondary"``
   * - ``level``
     - float or string containing a bounded integer
     - Master level to set on the group
     - ``0.5 or "50:100"``
   * - ``fade``
     - float
     - Optional. Fade time to apply the intensity change, in seconds.
     - ``2.0``
   * - ``delay``
     - float
     - Optional. Time to wait before applying the intensity change, in seconds.
     - ``2.0``

get_content_target_info
=======================

``get_content_target_info(callback)``

Returns an object with a single ``content_targets`` attribute, which has an array value. Each item in the array is a Content Target object with the same attributes as in the HTTP :ref:`content-target-http-get` response.

For example:

.. code-block:: js

   Query.get_content_target_info(c => {
     let level = c.content_targets[0].level // level of primary content target
   })
