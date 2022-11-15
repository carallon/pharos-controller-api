Command
#######

Methods
*******

.. _command-http-post:

POST
====

Run a Lua script or pass a command to the command line parser on the controller.

.. note:: The Command Line Parser must be enabled in the web interface settings of the current project, else this endpoint will not be available.

``POST /api/cmdline``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``input``
     - string
     - The script to parse or run.

For example:

.. code-block:: json

   {
     "input": "tl = 1 get_timeline(tl):start()"
   }

Response
--------

If the Command Line Parser is enabled in the web interface settings of the current project then a 200 status code will be returned, along with the text ``Executed`` if the script was executed successfully. If an error occurred when attempting to run the script then the error string will be returned.

The response will be ``501 Not Implemented`` if the Command Line Parser is not enabled, or ``400 Bad Request`` if no project is loaded.
