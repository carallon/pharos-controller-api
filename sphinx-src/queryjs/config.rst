Config
######

Functions
*********

edit_config
===========

Edits the configuration of the controller.

``edit_config(params, callback)``

``params`` is expected to be an object with the same attributes as the HTTP :ref:`config-http-post` request.

The ``callback`` function will be passed the same object as is received from the HTTP :ref:`config-http-post` request.

get_config
==========

Returns information about the queried controller's configuration.

``get_config(callback)``

Returns an object with the same attributes as in the HTTP :ref:`config-http-get` response.

For example:

.. code-block:: js

   Query.get_config(config => {
     let year = config.year
   })
