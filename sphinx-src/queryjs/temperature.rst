Temperature
###########

Functions
*********

get_temperature
===============

``get_temperature(callback)``

Returns an object with the same attributes as in the HTTP :ref:`temperature-http-get` response.

For example:

.. code-block:: js

   Query.get_temperature(temp => {
     const ambient = temp.ambient_temp
   })
