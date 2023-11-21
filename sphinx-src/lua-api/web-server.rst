WebServer
#########

Information about the controller's web server is available in the ``web_server`` namespace. In trigger action scripts the ``web_server`` namespace is added directly to the environment; in IO modules it is in the ``controller`` namespace, i.e. ``controller.web_server``.

Properties
**********

The ``web_server`` namespace has the following properties:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Property
     - Value Type
     - Description
     - Value Example
   * - ``is_enabled``
     - boolean
     - True if the web server is enabled
     - ``true``
   * - ``http_port``
     - integer
     - The port the HTTP web server is listening on or 0 if disabled.
     - ``51346``
   * - ``https_port``
     - integer
     - The port the HTTPS web server is listening on or 0 if disabled.
     - ``56278``
