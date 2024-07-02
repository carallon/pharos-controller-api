Fan Speed
###########

Functions
*********

get_fan_speed
===============

``get_fan_speed(callback)``

Returns an object with the same attributes as in the HTTP :ref:`fan-speed-http-get` response.

For example:

.. code-block:: js

   Query.get_fan-speed(fan_speeds => {
     const fan_1_speed = fan_speeds.fan_1
   })
