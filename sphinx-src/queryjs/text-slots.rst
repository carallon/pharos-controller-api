Text Slots
##########

Functions
*********

set_text_slot
=============

Set the value of a text slot used in the project, which will propagate to all controllers in a project.

``set_text_slot(params, callback)``

``params`` is expected to be an object with the same attributes as the HTTP :ref:`text-slot-http-put` request.

get_text_slot
=============

Returns data about the text slots in the project and their current values.

``get_text_slot(callback[, filter])``

Returns an object with a single ``text_slots`` attribute, which has an array value. Each item in the array is a Text Slot object with the same attributes as in the HTTP :ref:`text-slot-http-get` response.

``filter`` can be used to filter which text slots are returned and is expected to be an object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
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
