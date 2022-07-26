RDM Discovery
#############

Functions
*********

start_rdm_discovery
===================

Request to start a full RDM discovery. Results are available via :ref:`websocket_subscribe_rdm_discovery`.

``start_rdm_discovery(params, callback)``

``params`` is expected to be an object with the same attributes as the HTTP :ref:`rdm-discovery-http-post` request.
