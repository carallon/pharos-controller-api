Controller
##########

Functions
*********

get_controller_info
===================

``get_controller_info(callback)``

Returns an object with a single ``controllers`` attribute, which has an array value. Each item in the array is a Controller object with the same attributes as in the HTTP :ref:`controller-http-get` response.

For example:

.. code-block:: js

   Query.get_controller_info(data => {
        for(index in data.controllers) {
          console.log("Controller " + index + " name is " + data.controllers[index].name);
        }
   });

Will print out the name of each controller to the console.
