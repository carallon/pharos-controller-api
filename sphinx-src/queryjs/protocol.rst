Protocol
########

Functions
*********

get_protocols
=============

Returns all the universes in the project on the queried controller.

``get_protocols(callback)``

Returns an object with a single ``outputs`` attribute, which has an array value. Each item in the array is a Protocol object with the same attributes as in the HTTP :ref:`protocol-http-get` response.

For example:

.. code-block:: js

   Query.get_protocols(p => {
     const protocol_name = p.outputs[0].name // name of the first protocol
   })
