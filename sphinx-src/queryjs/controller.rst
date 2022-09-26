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

   Query.get_controller_info(controller => {
     let name = controller[0].name // name of the first controller
   })
