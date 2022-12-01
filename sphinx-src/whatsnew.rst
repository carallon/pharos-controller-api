What's New
##########

v6.0
****

* Breaking change to HTTP authentication, using new :doc:`http-api/authentication/authenticate` endpoint.
* Add :doc:`http-api/factory-reset` HTTP endpoint.
* Remove ``password`` from the HTTP :ref:`config <config-http-post>` response.

.. only:: designer

    * Breaking change to setting colour overrides with new :ref:`override-colour-json` object in :ref:`HTTP <override-http-put>` and :ref:`JavaScript <set-group-override-queryjs>`.
    * New snapshot functionality when setting colour overrides in :ref:`HTTP <override-http-put>` and :ref:`JavaScript <set-group-override-queryjs>`.
    * Add :doc:`http-api/rdm-discovery` HTTP endpoint and :doc:`queryjs/rdm-discovery` JavaScript function.
    * Add :doc:`http-api/rdm-get` HTTP endpoint and :doc:`queryjs/rdm-get` JavaScript function.
    * Add :doc:`http-api/rdm-set` HTTP endpoint and :doc:`queryjs/rdm-set` JavaScript function.
    * Add EDN protocols to Lua :ref:`Lua_disable_output`.

.. only:: expert

    * Breaking change to setting colour overrides with new :ref:`override-colour-json` object in :ref:`HTTP <override-http-put>`.
    * New snapshot functionality when setting colour overrides in :ref:`HTTP <override-http-put>`.
    * Add :doc:`http-api/rdm-discovery` HTTP endpoint.
    * Add :doc:`http-api/rdm-get` HTTP endpoint.
    * Add :doc:`http-api/rdm-set` HTTP endpoint.

.. only:: designer

    v5.0
    ****

    * Added controller propagation to certain HTTP API requests and query.js functions.
    * ``memory_free`` changed to ``memory_available`` in the HTTP & JavaScript :doc:`http-api/system` information and in the Lua :doc:`lua-api/system` namespace.
    * :ref:`Lua_get_trigger_number` function added.
    * ``vlan_tag`` property added to Lua :doc:`lua-api/controller`.
    * ``is_network_primary`` property added to Lua :doc:`lua-api/controller`.
    * ``dns_servers`` property added to the Lua :doc:`lua-api/system` namespace.
