Project
#######

Functions
*********

get_project_info
================

Returns data about the current project.

``get_project_info(callback)``

Returns an object with the same attributes as in the HTTP :ref:`project-http-get` response.

For example:

.. code-block:: js

   Query.get_project_info(project => {
     const author = project.author
   })
