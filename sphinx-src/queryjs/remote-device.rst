Remote Device
#############

Functions
*********

get_remote_device_info
======================

Returns data about all the remote devices in the project.

``get_remote_device_info(callback)``

Returns an object with a single ``remote_devices`` attribute, which has an array value. Each item in the array is a Remote Device object with the same attributes as in the HTTP :ref:`remote-device-http-get` response.

For example:

.. code-block:: js

   Query.get_remote_device_info(r => {
     const type = r.remote_devices[0].type // type of the first remote device
   })
