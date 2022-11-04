Timeline
########

Functions
*********

start_timeline
==============

``start_timeline(params, callback)``

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
     - Timeline number
     - ``5``

For ``callback`` please see `JavaScript Command Callback`_.

release_timeline
================

``release_timeline(params, callback)``

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
     - Timeline number
     - ``5``
   * - ``fade``
     - float
     - Optional. Release fade time in seconds. If not provided, the default fade time will be used.
     - ``2.0``

For ``callback`` please see `JavaScript Command Callback`_.

toggle_timeline
===============

``toggle_timeline(params, callback)``

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
     - Timeline number
     - ``5``
   * - ``fade``
     - float
     - Optional. The release fade time in seconds to apply if the toggle action results in the timeline being released. If not provided, the default fade time will be used.
     - ``2.0``

For ``callback`` please see `JavaScript Command Callback`_.

pause_timeline
==============

``pause_timeline(params, callback)``

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
     - Timeline number
     - ``5``

For ``callback`` please see `JavaScript Command Callback`_.

resume_timeline
===============

``resume_timeline(params, callback)``

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
     - Timeline number
     - ``5``

For ``callback`` please see `JavaScript Command Callback`_.

pause_all
=========

Pause all timelines in the project which are currently running. Propagates to all controllers in a project.

``pause_all(callback)``

For ``callback`` please see `JavaScript Command Callback`_.

resume_all
==========

Resume all timelines in the project which are currently paused. Propagates to all controllers in a project.

``resume_all(callback)``

For ``callback`` please see `JavaScript Command Callback`_.

release_all_timelines
=====================

``release_all_timelines(params, callback)``

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
     - Optional. Timeline group name: ``A``, ``B``, ``C`` or ``D``. Prepend the group name with ``!`` to apply the action to all groups *except* the specified group, e.g. ``!A``.
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

set_timeline_rate
=================

``set_timeline_rate(params, callback)``

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
     - Timeline number
     - ``5``
   * - ``rate``
     - string
     - A string containing a floating point number or a bounded integer, where 1.0 means the timeline's default rate.
     - ``"0.1"`` or ``"10:100"``

For ``callback`` please see `JavaScript Command Callback`_.

set_timeline_position
=====================

``set_timeline_position(params, callback)``

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
     - Timeline number
     - ``5``
   * - ``position``
     - string
     - A string containing a floating point number or a bounded integer, representing a fraction of the timeline length.
     - ``"0.1"`` or ``"10:100"``

For ``callback`` please see `JavaScript Command Callback`_.

get_timeline_info
=================

``get_timeline_info(callback[, num])``

Returns data about the timelines in the project and their state on the controller.

Returns an object with a single ``timelines`` attribute, which has an array value. Each item in the array is a Timeline object with the same attributes as in the HTTP GET response.

``num`` can be used to filter which timelines are returned and is expected to be an object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - string **or** integer
     - Define the numbers of the timeline that should be returned
     - ``"1,2,5-9"`` **or** ``5``

For example:

.. code-block:: js

   Query.get_timeline_info(t => {
     let name = t.timelines[0].name // name of the first timeline returned
   }, {"num":"1-4"})


JavaScript Command Callback
***************************

.. include:: snippets/js-command-callback.rst
