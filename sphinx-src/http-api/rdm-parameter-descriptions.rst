RDM Parameter Descriptions
##########################

Methods
*******

.. _rdm_parameter_descriptions-http-get:

GET
===

Get RDM parameter descriptions cached from the latest RDM discovery. Currently only values for ``DMX_PERSONALITY_DESCRIPTION`` are returned.

``GET /api/rdm/parameter_descriptions``

Returns a JSON object with keys that correspond to each unique device variant found during RDM discovery. Each entry is an object containing cached parameter descriptions.

.. code-block:: json

  {
    "25972-517-17170449": {
      "DMX_PERSONALITY_DESCRIPTION": [
        "5 Channel",
        "Direct",
        "1 Channel",
        "RGB"
      ]
    }
  }


Device Variant String Format
****************************

An RDM device variant string is structured as follows, with each of the 3 tokens formatted as decimal integers.

``{manufacturer ID}-{model ID}-{software version ID}``
