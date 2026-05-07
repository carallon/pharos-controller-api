Trigger
#######

.. include:: snippets/functions-require-project.rst

Functions
*********

fire_trigger
==============

``fire_trigger(params, callback)``

``params`` is expected to be an object with the same attributes as the HTTP :ref:`trigger-http-post` request.


get_trigger_info
================

``get_trigger_info(callback[, params])``

Returns an object with a single ``triggers`` attribute, which has an array value. Each item in the array is a Trigger object with the same attributes as in the HTTP :ref:`trigger-http-get` response.

``params`` is an optional argument object, which can be used to filter the type of trigger returned.
The object should have a single member, ``type`` which should be a string of the trigger type to filter by.

For example, the following code will search for triggers of type **Startup**:

.. code-block:: js

   Query.get_trigger_info(t => {
      let name = t.triggers[0].name // name of first startup trigger returned
   },
   {
      type: "Startup"
   })
