IO Module
#########

The IO Module channel provides status updates from the IO modules via the IO module *Instance Status Variables* - see the IO module developer guide for more details.


Subscribe Message
-----------------

.. code-block:: json

   {
      "subscribe": "io_module"
   }


Change Message
--------------

When any IO module data changes, a change message is sent containing:

* A `data` object containing modules, which is an array of module objects with an ID and name

* An `instances` array which contains one object for every IO module instance in the project. Each instance includes:

  * An ID for the instance

  * A module_id which ties it back to one of the reported module types

  * The user name for the module instance

  * An array of status values as provided by the IO module status API

    * A status consists of a string key and a value.


.. code-block:: json

   {
      "data": {
         "modules": [
            {
               "id": 1,
               "name": "Wait"
            },
            {
               "id": 2,
               "name": "Repeat"
            }
         ],
         "instances": [
            {
               "id": 1,
               "module_id": 1,
               "name": "Wait Instance 1",
               "status": [
                  {
                     "key": "currentWaits",
                     "label": "Current Waits"
                  }
               ]
            },
            {
               "id": 2,
               "module_id": 2,
               "name": "Repeat Module",
               "status": [
                  {
                     "key": "description",
                     "label": "Description",
                     "value": "Enqueue trigger 501, wait 30s and repeat forever"
                  },
                  {
                     "key": "currentCount",
                     "label": "Current Occurrence Count",
                     "value": "136"
                  },
                  {
                     "key": "lastFired",
                     "label": "Last Fired",
                     "value": "12:25:59 on 2/5/2025"
                  },
                  {
                     "key": "currentStatus",
                     "label": "Status",
                     "value": "Counting Up"
                  }
               ]
            }
         ]
      },
      "id": 1,
      "request": "io_module"
   }
