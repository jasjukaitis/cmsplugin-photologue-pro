########################
cmsplugin-photologue-pro
########################

This is another photologue plugin for Django CMS.


Requirements
============

  * Django
  * django-photologue
  * django-cms


Installation
============

Using PyPI you can simply type into a terminal:

    pip install cmsplugin-photologue-pro

or

    easy_install cmsplugin-photologue-pro


Configuration
=============

Add ``photologue`` and ``cmsplugin_photologue_pro`` to the list of
``INSTALLED_APPS`` in your ``settings.py`` file. Don't forget to syncdb your
database or migrate if you're using ``south``.


Author
======

Copyright 2012 Raphael Jasjukaitis <webmaster@raphaa.de>

Released under the BSD license.
