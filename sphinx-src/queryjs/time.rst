Time
####

Functions
*********

get_current_time
================

``get_current_time(callback)``

Returns an object with the same attributes as in the :ref:`time-http-get` GET response.

For example:

.. code-block:: js

   Query.get_current_time(time => {
     const uptime = time.uptime
   })
