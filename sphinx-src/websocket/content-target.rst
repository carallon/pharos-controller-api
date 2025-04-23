Content Target
##############

The ``content-target`` channel is available on |VLC| and |VLC+| controllers only.

It provides a list of content targets, and updates if the master level of a content target changes.


Subscribe Message
-----------------

.. code-block:: json

   {
      "subscribe": "content_target"
   }



Change Message
--------------

When the master level of a content target is changed, an update message will be sent with an array ``content_targets`` in the data. Each object has keys:

.. include:: ../snippets/json-attributes-content-target.rst

For example:

.. code-block:: json

    {
        "request": "content_target",
        "id": 5,
        "data": {
            "content_targets": [
                {
                    "name": "Primary",
                    "level": 100
                },
                {
                    "name": "Secondary",
                    "level": 100
                },
                {
                    "name": "Target 3",
                    "level": 100
                },
                {
                    "name": "Target 4",
                    "level": 100
                },
                {
                    "name": "Target 5",
                    "level": 100
                },
                {
                    "name": "Target 6",
                    "level": 100
                },
                {
                    "name": "Target 7",
                    "level": 100
                },
                {
                    "name": "Target 8",
                    "level": 100
                }
            ]
        }
    }
