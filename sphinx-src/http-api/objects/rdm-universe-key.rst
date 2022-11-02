RDM Universe Key
################

Used to specify the target universe for RDM operations. It is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``protocol``
     - integer
     - Output protocol (see `Enumerated Protocols`_).
   * - ``index``
     - integer
     - Only required for protocols ``DMX`` and ``ART-NET``.
   * - ``remote_device_num``
     - integer
     - Only required for protocol ``EDN``. The remote device number of the EDN node.
   * - ``remote_device_type``
     - integer
     - Only required for protocol ``EDN``. The type of EDN as defined in `Enumerated EDN Device Types`_.
   * - ``port``
     - integer
     - Only required for protocol ``EDN``. The port on the EDN.

Enumerated Protocols
********************

.. include:: ../../snippets/enumerated-protocols.rst

Enumerated EDN Device Types
***************************

.. include:: ../../snippets/enumerated-edn-types.rst
