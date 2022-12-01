DALI Error
##########

The DALI error object has the following attributes:

.. list-table::
   :widths: 5 2 10 4
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``address``
     - integer
     - The DALI bus address of the device with the error
     - ``12``
   * - ``test``
     - string
     - The test that discovered the error
     - ``"Function"``
   * - ``error``
     - string
     - A description of the DALI error
     - ``"Battery Duration"``
   * - ``fixed``
     - boolean
     - Whether the error has been fixed. Once fixed, the error remains in the list until it is retested.
     - ``true``
