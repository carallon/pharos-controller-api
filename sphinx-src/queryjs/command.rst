Command
#######

Functions
*********

run_command
===========

Run a Lua script or pass a command to the command line parser on the controller.

.. note:: The Command Line Parser must be enabled in the web interface settings of the current project, else this function will not be available.

``run_command(params, callback)``

``params`` is expected to be an object with the same attributes as the HTTP :ref:`command-http-post` request.

Returns ``Executed`` if the script was executed successfully or an error string if not.
