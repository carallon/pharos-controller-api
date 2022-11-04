Config
######

Methods
*******

.. _config-http-post:

POST
====

Edits the configuration of the controller.

``POST /api/config``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``ip``
     - string
     - Optional. Set the controller's IP address (management interface)
     - ``"192.168.1.3"``
   * - ``subnet_mask``
     - string
     - Optional. Set the controller's subnet mask (management interface)
     - ``"255.255.255.0"``
   * - ``gateway``
     - string
     - Optional. Set the controller's gateway address (management interface)
     - ``"192.168.1.1"``
   * - ``dhcp_enabled``
     - boolean
     - Optional. Set whether the controller is assigned its IP address automatically by DHCP
     - ``true``
   * - ``name_server_1``
     - string
     - Optional. Set the primary name server address
     - ``"192.168.1.1"``
   * - ``name_server_2``
     - string
     - Optional. Set the secondary name server address
     - ``"8.8.8.8"``
   * - ``http_port``
     - integer
     - Optional. Set the port opened for HTTP access to the controller's web server
     - ``80``
   * - ``https_port``
     - integer
     - Optional. Set the port opened for HTTPS access to the controller's web server
     - ``443``
   * - ``year``
     - integer
     - Optional. Set the year of the current date on the controller's clock
     - ``2021``
   * - ``month``
     - integer
     - Optional. Set the month of the current date on the controller's clock (1-12)
     - ``4``
   * - ``day``
     - integer
     - Optional. Set the day of the current date on the controller's clock (1-31)
     - ``25``
   * - ``hour``
     - integer
     - Optional. Set the hour component of the current time on the controller's clock (0-23)
     - ``13``
   * - ``minute``
     - integer
     - Optional. Set the minute component of the current time on the controller's clock (0-59)
     - ``21``
   * - ``second``
     - integer
     - Optional. Set the second component of the current time on the controller's clock (0-59)
     - ``46``
   * - ``watchdog_enabled``
     - boolean
     - Optional. Set whether the controller's hardware watchdog is enabled
     - ``true``
   * - ``log_level``
     - integer
     - Optional. Set the level of verbosity of the controller's log (1-5)
     - ``3``
   * - ``syslog_enabled``
     - boolean
     - Optional. Set whether the controller will send its log to a syslog server
     - ``false``
   * - ``syslog_ip``
     - string
     - Optional. Set the IP address of a third party syslog server
     - ``"192.168.1.2"``
   * - ``ntp_enabled``
     - boolean
     - Optional. Set whether the controller will fetch the current time automatically from an NTP server
     - ``true``
   * - ``ntp_ip``
     - string
     - Optional. Set the IP address of a third party NTP server
     - ``"192.168.1.1"``
   * - ``password``
     - string
     - Optional. Change the admin password on the controller.
     - ``"mySup3rS3cr3tP455w0rd!"``

If the response status code is 200 (OK), the response body will be a JSON object with a ``restart`` attribute. The value of ``restart`` is boolean. If ``true``, the controller will reset itself imminently in order to apply the changes.

.. _config-http-get:

GET
===

Returns information about the queried controller's configuration.

``GET /api/config``

Returns a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``ip``
     - string
     - Controller IP address (management interface)
     - ``"192.168.1.3"``
   * - ``subnet_mask``
     - string
     - Controller subnet mask (management interface)
     - ``"255.255.255.0"``
   * - ``gateway``
     - string
     - Gateway address (management interface)
     - ``"192.168.1.1"``
   * - ``dhcp_enabled``
     - boolean
     - Whether the controller is assigned its IP address automatically by DHCP
     - ``true``
   * - ``name_server_1``
     - string
     - Primary name server address
     - ``"192.168.1.1"``
   * - ``name_server_2``
     - string
     - Secondary name server address
     - ``"8.8.8.8"``
   * - ``http_port``
     - integer
     - Port opened for HTTP access to the controller's web server
     - ``80``
   * - ``https_port``
     - integer
     - Port opened for HTTPS access to the controller's web server
     - ``443``
   * - ``year``
     - integer
     - Year of the current date, according to the controller's clock
     - ``2021``
   * - ``month``
     - integer
     - Month of the current date, according to the controller's clock (1-12)
     - ``4``
   * - ``day``
     - integer
     - Day of the current date, according to the controller's clock (1-31)
     - ``25``
   * - ``hour``
     - integer
     - Hour component of the current time, according to the controller's clock (0-23)
     - ``13``
   * - ``minute``
     - integer
     - Minute component of the current time, according to the controller's clock (0-59)
     - ``21``
   * - ``second``
     - integer
     - Second component of the current time, according to the controller's clock (0-59)
     - ``46``
   * - ``watchdog_enabled``
     - boolean
     - Whether the controller's hardware watchdog is enabled
     - ``true``
   * - ``log_level``
     - integer
     - Level of verbosity of the controller's log (1-5)
     - ``3``
   * - ``syslog_enabled``
     - boolean
     - Whether the controller is sending its log to a syslog server
     - ``false``
   * - ``syslog_ip``
     - string
     - IP address of a third party syslog server
     - ``"192.168.1.2"``
   * - ``ntp_enabled``
     - boolean
     - Whether the controller is fetching current time automatically from an NTP server
     - ``true``
   * - ``ntp_ip``
     - string
     - IP address of a third party NTP server
     - ``"192.168.1.1"``
