Lua Variable
############

Methods
*******

.. _lua-variable-http-get:

GET
===

Returns the current value of specified Lua variables.

``GET /api/lua?variables=luaVariables``

``luaVariables`` is expected to be a string or comma-separated list of strings, where each string is a Lua variable name.

Returns a JSON object with the Lua variables and their values as its key/value pairs - the Lua variable names are the keys.

For example, in a project that creates variables called ``bob`` and ``alice``, ``GET /api/lua?variables=bob,alice`` could return a JSON object as follows:

.. code-block:: json

   {
     "alice": 1234,
     "bob": "a string variable"
   }
