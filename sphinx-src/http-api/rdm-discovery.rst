RDM Discovery
#############

Methods
*******

.. _rdm-discovery-http-post:

POST
====

Request to start a full RDM discovery. A ``202`` response will be returned if the request has been successfully queued. Results are available via a websocket subscription (see :ref:`websocket_subscribe_rdm_discovery`).

``POST /api/rdm/discovery``

Payload is a JSON object with a single ``universe`` attribute, which can either be a string in the `Universe Key String Format`_ or an :doc:`objects/rdm-universe-key` object.

For example, to start a full discovery on DMX universe 2, the request payload could be:

.. code-block:: json

   {
     "universe": "dmx:2"
   }

or, alternatively:

.. code-block:: json

   {
     "universe": {
       "protocol": 1,
       "index": 2
     }
   }

To start RDM discovery on the first port of the EDN 20 with number 4 in the project, the request payload could be:

.. code-block:: json

   {
     "universe": "edn:edn20:4:1"
   }

or, alternatively:

.. code-block:: json

   {
     "universe": {
       "protocol": 128,
       "remote_device_type": 109
     }
   }


PUT
===

Request to start an RDM discovery update, which is faster if a full RDM discovery has already been performed with a :ref:`rdm-discovery-http-post` request. A ``202`` response will be returned if the request has been successfully queued. Results are available via a websocket subscription (see :ref:`websocket_subscribe_rdm_discovery`).

``PUT /api/rdm/discovery``

Payload is a JSON object with a single ``universe`` attribute, which can either be a string in the `Universe Key String Format`_ or an object with the same attributes as for the :ref:`rdm-discovery-http-post` request.


GET
===

Returns the cached results of the last RDM discovery operation.

``GET /api/rdm/discovery?universe=universeId``

``universe`` specifies which output universe to fetch cached RDM discovery data for. Its value is a string in the `Universe Key String Format`_.

Returns a JSON object with a ``devices`` attribute, which has an array value. Each item in the array is an :doc:`objects/rdm-device-info` object.


Universe Key String Format
**************************

.. include:: ../snippets/universe-key-string-format-rdm.rst
