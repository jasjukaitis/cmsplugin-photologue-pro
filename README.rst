####################
cmsplugin-photologue
####################

This is an photo gallery plugin for Django CMS.


Requirements
============

  * Django
  * django-photologue
  * django-cms


Installation
============

Using PyPI you can simply type into a terminal:

    pip install cmsplugin-photologue

or

    easy_install cmsplugin-photologue


Configuration
=============

Add ``photologue`` and ``cmsplugin_photologue`` to the list of
``INSTALLED_APPS`` in your ``settings.py`` file. Don't forget to syncdb your
database or migrate if you're using ``south``.


Author
======

Copyright 2012 Raphael Jasjukaitis <webmaster@raphaa.de>

Released under the BSD license.
