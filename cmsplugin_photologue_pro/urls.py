# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('cmsplugin_photologue_pro.views',
    url(r'^$', 'overview', name='photologue_overview'),
    url(r'^(?P<album>\d+)/$', 'album', name='photologue_album'),
    url(r'^(?P<album>\d+)/(?P<photo>\d+)/$', 'photo', name='photologue_photo'),
)
