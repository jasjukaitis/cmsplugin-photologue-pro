# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('cmsplugin_photologue.views',
    url(r'^$', 'overview', name='overview'),
    url(r'^(?P<album>\d)/$', 'album', name='album'),
    url(r'^(?P<album>\d)/(?P<photo>\d)/$', 'photo', name='photo'),
)
