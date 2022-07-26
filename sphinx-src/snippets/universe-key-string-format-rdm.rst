A universe key string for RDM takes the form:

* ``protocol:index`` for protocols ``dmx`` and ``art-net``;
* ``protocol:remoteDeviceType:remoteDeviceNum:port`` for protocol ``edn``.

Where:

* ``remoteDeviceType`` can be ``edn10`` or ``edn20``;
* ``remoteDeviceNum`` is an integer;
* ``port`` is an integer.

For example:

* ``"dmx:1"``
* ``"edn:edn20:1:5"``
