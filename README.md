makeappmessages
===============

makeappmessages is a simple Django app that adds **makeappmessages** management command to create local message files only for project custom apps (apps in project directory).

How to use:
===========
- add **makeappmessages** to INSTALLED_APPS
- run **manage.py makeappmessages --app app_name1 app_name2** to create local message files for app_name1, app_name2
or
- run **manage.py makeappmessages** to create local message files for all apps in project directory

**makeappmessages** command is a wrapper to the native django's **makemessages** command so it supports any arguments that **makemessages** does.
