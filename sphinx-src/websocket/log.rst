Log
###

The log features allow subscription to messages sent to the controllers log.

Subscribe Message
-----------------

.. code-block:: json

   {
      "subscribe": "log"
   }

Log Message Levels
------------------

Log messages are assigned one of the following levels:

.. list-table::
  :widths: 75 25
  :header-rows: 1

  * - Log Level
    - Value
  * - Critical
    - 2
  * - Terse
    - 3
  * - Normal
    - 4
  * - Extended
    - 5
  * - Verbose
    - 6
  * - Debug
    - 7

Log Message Categories
----------------------

.. list-table::
  :widths: 75 25
  :header-rows: 1

  * - Log Category
    - Value
  * - System
    - 16
  * - Project
    - 17
  * - Time
    - 18
  * - Output
    - 19
  * - IO
    - 20
  * - Trigger
    - 21
  * - Controller API
    - 22
  * - DALI
    - 23

Change Message
--------------

The log data is formatted as follows:

* Special character ``\u0007`` is sent to indicate the start of a log entry

* It is followed by two values encoded as characters:

  * The log type.

  * The log level.

* Then the offset from UTC time to controller local time, represented as a value in minutes offset from -24 hours, in hexadecimal.
* Then a space and the UTC timestamp of the event.
* Then the log message text.

For example:

.. code-block::

   \u0007\u0015\u00045dc 68907857ACTION Start Timeline Timeline 2\n

Indicates:

* Start of log message
* A log type of ``0x15`` = ``21`` = ``Trigger``.
* A log level of ``0x4`` = ``Normal``.
* An offset of ``0x5dc`` = ``-(24*60) + 1500`` = ``+60 minutes offset from UTC``.
* A UTC timestamp of ``0x68907857`` = ``Monday, 4 August 2025 09:07:35``.

So this message should be recorded as occurring on Monday, 4th August 2025 at 10:07:35 local time.

A more complete example may have multiple messages packed into the data block as shown below:

.. code-block:: json

   {
      "request": "log",
      "id": 1,
      "data": {
         "log": "\u0007\u0015\u00045dc 68907857ACTION Start Timeline Timeline 2\n\u0007\u0016\u00045dc 68907857Web API: Enqueue trigger 2"
      }
   }
