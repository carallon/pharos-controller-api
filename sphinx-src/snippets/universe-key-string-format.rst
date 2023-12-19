A universe key string takes the form:

.. only:: expert

    * ``protocol:index`` where:

      * ``protocol`` is ``dmx``, ``sacn``, or ``art-net``;

      * ``index`` is the index of the output port, 1 or 2, matching the port on the Expert Control device


    For example:

    * ``"dmx:1"`` refers to port 1 on the Expert Controller

.. only:: designer

    * ``protocol:index`` for protocols ``dmx``, ``pathport``, ``sacn``, ``art-net``;
    * ``protocol:kinetPowerSupplyNum:kinetPort`` for protocol ``kinet``;
    * ``protocol:remoteDeviceType:remoteDeviceNum`` for protocol ``rio-dmx``;
    * ``protocol:remoteDeviceType:remoteDeviceNum:port`` for protocols ``edn``, ``edn-spi``.

    Where:

    * ``kinetPowerSupplyNum`` is an integer;
    * ``kinetPort`` is an integer;
    * ``remoteDeviceType`` can be ``rio08``, ``rio44`` or ``rio80``, ``edn10`` or ``edn20``;
    * ``remoteDeviceNum`` is an integer;
    * ``port`` is an integer.

    For example:

    * ``"dmx:1"``
    * ``"rio-dmx:rio44:1"``
