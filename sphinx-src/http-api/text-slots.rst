Text Slots
##########

Methods
*******

.. _text-slot-http-put:

PUT
===

Set the value of a text slot used in the project, which will propagate to all controllers in a project.

``PUT /api/text_slot``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - Text slot name
     - ``"myTextSlot"``
   * - ``value``
     - string
     - New value for the text slot.
     - ``"Hello World!"``

.. _text-slot-http-get:

GET
===

Returns data about the text slots in the project and their current values.

``GET /api/text_slot[?names=slotNames]``

``slotNames`` can be used to filter which test slots are returned and is expected to be either a single string or an array of strings.

Returns a JSON object with a single ``text_slots`` attribute, which has an array value. Each item in the array is a Text Slot object with the following attributes:

.. list-table::
   :widths: 3 3 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Value Example
   * - ``name``
     - string
     - ``"text"``
   * - ``value``
     - string
     - ``"example"``

