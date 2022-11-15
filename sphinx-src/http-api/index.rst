HTTP API
########

|Vendor| controllers provide an HTTP API to query and control the current project and the controller itself.

Authentication
**************

|Vendor| controllers have user accounts, each of which can belong to different security groups, which in turn control access to parts of the HTTP API. The HTTP API has a series of :doc:`endpoints <authentication/index>` to allow clients to authenticate users with the controller.

.. toctree::
   :hidden:

   authentication/index

Querying and Controlling
************************

The endpoints provided in the HTTP API for querying and controlling the controller and its current project are detailed in the following sections:

.. toctree::
   :maxdepth: 1

   beacon
   channel
   command
   config
   content-targets
   controller
   factory-reset
   group
   input
   log
   lua-variable
   output
   override
   project
   protocol
   rdm-discovery
   rdm-get
   rdm-set
   remote-device
   replication
   reset
   scene
   system
   temperature
   text-slots
   time
   timeline
   trigger

.. toctree::
   :hidden:

   objects/index
