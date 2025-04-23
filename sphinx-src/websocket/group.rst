Group
#####

The Group subscription allows you to subscribe to changes of master intensity value for all groups.


Subscribe Message
-----------------

.. code-block:: json

   {
      "subscribe": "group"
   }


Change Message
--------------

When a group master intensity level changes, a message is sent out with the following parameters in the ``data`` part of the JSON object:

.. include:: ../snippets/json-attributes-group.rst

Example:

.. code-block:: json

   {
      "broadcast": "group",
      "data": {
         "level": 67,
         "name": "Group 1",
         "num": 1
      }
   }
