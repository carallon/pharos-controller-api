Project File
############

The controller allows you to upload or download the current project file, allowing the project in use to be switched out.

Methods
*******

GET
===

Downloads the currently running project file.

``GET /api/project/file``

Returns the project file (as type application/vnd.pharos).

POST
====

Uploads a project file, which will trigger the controller to switch to the new file.

.. warning::

   The file to be uploaded **must** be exported from Designer for the project using the *Export Project For Upload* button in Designer under the *Network* tab. You can **not** load a saved Designer project file directly.

``POST /api/project/file``

Uploads a project file to the controller. The body of the request should be the exported project file as binary data.

Note that the ``Content-Type`` header should be set to ``application/vnd.pharos``; and the ``Content-Length`` header should be set to the size of the project file.
