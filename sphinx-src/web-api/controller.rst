Controller
##########

Returns data about the controllers in the project.

HTTP
****

GET
===

``GET /api/controller``

Returns a JSON object with a single ``controllers`` attribute, which has an array value. Each item in the array is a Controller object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Controller number
     - ``1``
   * - ``type``
     - string
     - Controller type, e.g. "LPC" or "TPC"
     - ``"LPC"``
   * - ``name``
     - string
     - Controller user name, or the default name if none is set
     - ``"Controller 1"``
   * - ``serial``
     - string
     - Serial number of the controller
     - ``"009060"``
   * - ``ip_address``
     - string
     - IP address of the controller if the controller is discovered; empty if the controller is not discovered or is the queried controller
     - ``"192.168.1.3"`` or ``""``
   * - ``online``
     - boolean
     - Whether the controller is detected as online on the local network
     - ``true``
   * - ``is_network_primary``
     - boolean
     - Whether the controller is set as the network primary in the project
     - ``true``

JavaScript
**********

get_controller_info
===================

``get_controller_info(callback)``

Returns an object with a single ``controllers`` attribute, which has an array value. Each item in the array is a Controller object with the same attributes as in the HTTP GET response.

For example:

.. code-block:: js

   Query.get_controller_info(controller => {
     let name = controller[0].name // name of the first controller
   })
