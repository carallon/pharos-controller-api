.. _htaccess:

.htaccess Files (**deprecated**)
################################

.. attention:: The use of .htaccess files in API v6 onwards has been deprecated, although existing files will still function as before. Please see :ref:`webconfig file<webconfig>` for the superseding functionality.

``.htaccess`` files can be used to control user access to certain parts of a custom web interface. The filename is ``.htaccess``, the leading full stop (.) indicating that this is a hidden file.

When a user navigates to the controller's IP Address, the ``.htaccess`` file(s) within the custom web interface files will determine which parts of the web interface the user can get to, based on their login details.

Example Web Interface Structure
===============================

Below is an example of a custom web interface file structure::

    Root Directory
    ├── index.html
    ├── login.html
    ├── .htaccess
    ├── groups
    ├── admin
    │ ├── .htaccess
    │ ├── index.html
    │ └── admin.html

Files
=====

Top Level .htaccess file
++++++++++++++++++++++++

::

    AuthGroupFile groups
    AuthFormLoginRequiredLocation login.html

The ``AuthGroupFile`` line is used to link to the ``Groups`` file defined below.

The ``AuthLoginRequiredLocation`` line is used to define a custom login page (if the user isn't authorised). If this line isn't present then the default login page will be used. For more information about authentication, see :doc:`../web-api-authentication`.

Groups file
+++++++++++

::

    Admin: bob ted
    Guest: clarence simon

This file contains a list of the users in each group of the web interface. Each line takes the form ``GroupName: User1 User2 User3``. This applies to every folder, not just the one the .htaccess file is in. If a user is listed, here they must also be added to the web users in the web interface pane and given a password.

.htaccess file in admin folder
++++++++++++++++++++++++++++++

::

    DirectoryIndex admin.html
    Require group Admin

Within a folder, you can have an ``.htaccess`` file to define the groups that can access the files within the folder.

``DirectoryIndex`` defines the URL of the page to be served if the directory is requested. If it is not present then it defaults to a file named (in order of preference) ``index.xhtml``, ``index.html``, ``index.htm``, ``index.lp``, ``index.lsp``, ``index.lua``, ``index.cgi``, ``index.shtml`` or ``index.php``.

``Require group`` defines which group(s) are allowed to access the files in this folder.
