Lua Variable
############

Returns the current value of specified Lua variables.

HTTP
****

GET
===

``GET /api/lua?variables=luaVariables``

``luaVariables`` is expected to be a string or comma-separated list of strings, where each string is a Lua variable name.

Returns a JSON object with the Lua variables and their values as its key/value pairs - the Lua variable names are the keys.

For example, in a project that creates variables called ``bob`` and ``alice``, ``GET /api/lua?variables=bob,alice`` could return a JSON object as follows:

.. code-block:: json

   {
     "alice": 1234,
     "bob": "a string variable"
   }

JavaScript
**********

get_lua_variables
=================

``get_lua_variables(luaVariables, callback)``

Returns an object with the requested Lua variables and their values as key/value pairs, in the same manner as the HTTP request.

``luaVariables`` can be a string or an array of strings, where each string is a Lua variable name.

For example:

.. code-block:: js

   Query.get_lua_variables(["foo","bar"], v => {
     let foo = v.foo
     let bar = v.bar
   })
