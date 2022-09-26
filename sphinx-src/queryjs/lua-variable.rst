Lua Variable
############

Functions
*********

get_lua_variables
=================

Returns the current value of specified Lua variables.

``get_lua_variables(luaVariables, callback)``

Returns an object with the requested Lua variables and their values as key/value pairs, in the same manner as the HTTP :ref:`lua-variable-http-get` request.

``luaVariables`` can be a string or an array of strings, where each string is a Lua variable name.

For example:

.. code-block:: js

   Query.get_lua_variables(["foo","bar"], v => {
     let foo = v.foo
     let bar = v.bar
   })
