System
######

Functions
*********

get_system_info
===============

``get_system_info(callback)``

Returns an object with the same attributes as in the HTTP :ref:`system-http-get` response.

For example:

.. code-block:: js

   Query.get_system_info(system => {
     const capacity = system.channel_capacity
   })
