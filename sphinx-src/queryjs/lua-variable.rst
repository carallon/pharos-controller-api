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
The Lua variable must be directly accessible from the Lua global table.

For example:

.. code-block:: lua

   --[[ Lua definitions ]]--
   foo = 'spam'
   bar = {
      a = 'ham',
      b = 100
   }
   local baz = 'eggs'

.. code-block:: js

   /* Javascript Query */
   Query.get_lua_variables(["foo","bar"], v => {
     let foo = v.foo // foo contains "spam"
     console.log(typeof foo) // Output: "string"
     let bar = v.bar // bar contains a javascript object { a: "ham", b: 100 }
     console.log(typeof bar) // Output: "object"
     console.log(typeof bar.a) // Output: "string"
     console.log(typeof bar.b) // Output: "number"
   })

   // Invalid query, `a` is a child of `bar` and not directly accessible from the global table
   Query.get_lua_variables(["bar.a"], v => {})

   // Invalid query, `baz` is scoped locally, and inaccessible from the global table
   Query.get_lua_variables(["baz"], v => {})
