Trigger
#######

Functions
*********

fire_trigger
==============

``fire_trigger(params, callback)``

``params`` is expected to be an object with the same attributes as the HTTP :ref:`trigger-http-post` request.


get_trigger_info
================

``get_trigger_info(callback[, type])``

Returns an object with a single ``triggers`` attribute, which has an array value. Each item in the array is a Trigger object with the same attributes as in the HTTP :ref:`trigger-http-get` response.

``type`` is expected to be a string and can be used to filter the type of trigger returned. For example, ``"Timeline Started"`` would return only Timeline Started triggers in the project.

For example:

.. code-block:: js

   Query.get_trigger_info(t => {
     let name = t.triggers[0].name // name of first startup trigger returned
   }, "Startup")
