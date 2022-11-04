Trigger
#######

Methods
*******

.. _trigger-http-post:

POST
====

Fire a trigger in the project.

``POST /api/trigger``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - User number of the trigger to fire.
     - ``2``
   * - ``var``
     - string
     - Optional. Comma-separated to pass into the trigger.
     - e.g. a string ``"Foo"``; integers ``2,4,5``; multiple strings ``'"string1","string2","string3"'``
   * - ``conditions``
     - boolean
     - Optional. Whether to test the trigger's conditions before deciding to run its actions. Defaults to ``true``.
     - ``true``


.. _trigger-http-get:

GET
===

Returns the triggers in the project.

``GET /api/trigger?[type=triggerType]``

``triggerType`` is expected to be a string and can be used to filter the type of trigger returned. For example, ``"Timeline Started"`` would return only Timeline Started triggers in the project.

Returns a JSON object with a single ``triggers`` attribute, which has an array value. Each item in the array is a Trigger object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``type``
     - string
     - Trigger type
     - ``"Startup"``
   * - ``num``
     - integer
     - Trigger user number
     - ``1``
   * - ``name``
     - string
     - User-defined trigger name
     - ``"Initialise"``
   * - ``group``
     - string
     - Trigger group colour as a hex colour string
     - ``"#e18383"``
   * - ``description``
     - string
     - User-defined description of trigger
     - ``""``
   * - ``trigger_text``
     - string
     - Generated description of when the trigger will run, based on its properties
     - ``"At startup"``
   * - ``conditions``
     - array
     - Array of Condition objects (see below)
     - ``[{"text":"Before 12:00:00 every day"}]``
   * - ``actions``
     - array
     - Array of Action objects (see below)
     - ``[{"text":"Start Timeline 1"}]``

The Condition and Action objects have the following properties:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``text``
     - string
     - Generated description of the condition or action, based on its properties
     - ``"Start Timeline 1"``
