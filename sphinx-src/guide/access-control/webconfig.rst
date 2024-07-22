.. _webconfig:

.webconfig
##########

.. note:: This method should be used to configure access in the web interface for all versions of the controller API v6.0 onwards. This supersedes the use of ``.htaccess`` files.

The ``.webconfig`` file can be used to set properties of the custom web interface, scoped to folders in the web interface. It is written in the form of an ``.ini`` file, with each section representing a different folder in the custom web interface.

The file must be named ``.webconfig`` and located in the root directory of your custom interface.

The beginning of the file can contain sections for each path that needs custom rules. The path properties that can be defined are:

IndexFile
*********

This defines the URL of the page to be served if the directory is requested. If it is not present then it defaults to a file named (in order of preference) ``index.xhtml``, ``index.html``, ``index.htm``, ``index.lp``, ``index.lsp``, ``index.lua``, ``index.cgi``, ``index.shtml`` or ``index.php``.

Example: Setting an index file for the root of the custom web interface.

.. code-block:: ini

    [/]
    IndexFile = home.html

AllowedGroups
*************

This is a comma separated list of groups that have permission to access the folder.

For example, consider a custom web interface structured like this::

    Root Directory
    ├── index.html
    ├── login.html
    ├── .webconfig
    ├── admin
    │ ├── index.html
    ├── timeline
    │ ├── index.html
    │ ├── views
    │   ├── index.html
    │ ├── controls
    │   ├── index.html
    │   ├── timelineadmin
    │     ├── index.html

With a ``.webconfig`` file like this:

.. code-block:: ini

    [/admin]
    AllowedGroups = Admin
    [/timeline]
    AllowedGroups = Control, Status
    [/timeline/controls]
    AllowedGroups = Control
    [/timeline/controls/timelineadmin]
    AllowedGroups = Admin

This would lead to the following access abilities:

.. list-table::
   :widths: 55 15 15 15
   :header-rows: 1

   * - Folder
     - Admin
     - Control
     - Status
   * - ``/``
     - ✅
     - ✅
     - ✅
   * - ``/admin``
     - ✅
     - ❌
     - ❌
   * - ``/timeline``
     - ❌
     - ✅
     - ✅
   * - ``/timeline/views`` [#]_
     - ✅
     - ✅
     - ✅
   * - ``/timeline/controls``
     - ❌
     - ✅
     - ❌
   * - ``/timeline/controls/timelineadmin`` [#]_
     - ✅
     - ❌
     - ❌

.. [#] The ``/timeline/views`` folder has no specific restrictions in the ``webconfig`` file so it is available to all users.
.. [#] The ``/timeline/controls/timelineadmin`` folder specifically allows access by Admin, even though the parent folder doesn't.

LoginFile
*********

``LoginFile`` specifies the page that is loaded when a user tries to access a folder they don't have permission for.

This is used in conjunction with the above property to define a file that is shown when a user does not have access to a folder.

If no ``LoginFile`` is specified, the user will be presented with the standard login page (``/default/login.lsp``) in order to log in.

.. note:: This is only used when serving files. The Query.js library has alternative methods for handling auth errors.

Example: The ``login.html`` page will be show when trying to access files in ``/admin`` (if not logged into a user account with *Admin* permission) or ``/timeline`` (if not logged into a user account with *Control* or *Status* permission).

.. code-block:: ini

    [/admin]
    AllowedGroups = Admin
    LoginFile = login.html
    [/timeline]
    AllowedGroups = Control, Status
    LoginFile = login.html

The following can be used as a template for a ``login.html`` file:

.. code-block:: html

    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">
        </head>

        <body>
            <form action="/authenticate" method="POST">
                <input type="text" name="username" placeholder="Username">
                <input type="password" name="password" placeholder="Password">
                <button type="submit">Login</button>
            </form>
        </body>
    </html>

CustomGroups
************

In addition to the standard groups of Admin, Control and Status, up to 10 custom groups may be defined.

These are in a section marked as ``[Global]`` at the start of the file. A sample might look like this::

    [Global]
    CustomGroups = Maintenance, Cleaners

These additional groups can be used in the same manner as the standard groups shown above.

Once the custom groups have been added, individual users can have their group membership edited using the *Configuration* tab of the default web interface of the controller.
