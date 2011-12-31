# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PhotologueApphook(CMSApp):
    name = _(u'Photologue galleries')
    urls = ['cmsplugin_photologue.urls']

apphook_pool.register(PhotologueApphook)
