Text Slots
##########

HTTP
****

.. _text-slot-http-put:

PUT
===

Set the value of a text slot used in the project.

``PUT /api/text_slot``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
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

JavaScript
**********

set_text_slot
=============

Set the value of a text slot used in the project.

``set_text_slot(params, callback)``

``params`` is expected to be an object with the same attributes as the HTTP :ref:`text-slot-http-put` request.

get_text_slot
=============

Returns data about the text slots in the project and their current values.

``get_text_slot(callback[, filter])``

Returns an object with a single ``text_slots`` attribute, which has an array value. Each item in the array is a Text Slot object with the same attributes as in the HTTP GET response.

``filter`` can be used to filter which text slots are returned and is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``names``
     - string **or** array
     - Define the names of the text slots that should be returned, either as a single string or an array of strings
     - ``["test_slot1","anotherSlot"]`` **or** ``"test_slot1"``

For example:

.. code-block:: js

   Query.get_text_slot(t => {
     let value = t.text_slots[0].value // value of the first text slot returned
   }, {"names":["test_slot1","test_slot2"]})
