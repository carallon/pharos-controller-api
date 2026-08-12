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

* A `data` object containing:

  * An `instances` array which contains the values changed

    * An `id` for the instance

    * A `status` array containing the changed status key and the new value

.. code-block:: json

   {
      "broadcast": "io_module",
      "data": {
         "instances": [
            {
               "id": 2,
               "status": [
                  {
                     "key": "currentWaits",
                     "value": " {Fire trigger 1 in 9 seconds}"
                  }
               ]
            }
         ]
      }
   }

Request Response Message
------------------------

When a request is made for IO module data, for example using the request:

.. code-block:: json

   {
      "request": "io_module",
      "id": 1
   }

The following data fields are returned:

* A `data` object containing details of all the IO Modules and their instances

* A `modules` array containing

  * An `id` for the module

  * A `name` for the module

* An `instances` array which contains one object for every IO module instance in the project. Each instance includes:

  * An `id` for the instance

  * A `module_id` which ties it back to one of the reported module types

  * The `name` for the module instance

  * An array of `status` labels as provided by the IO module status API

    * A status consists of a string `key` and a `label`

.. code-block:: json

   {
      "id": 1,
      "request": "io_module",
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
      }
   }
