# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from cms.models.pagemodel import Page
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_photologue_pro import models as pluginmodels
from photologue import models
import re


class AlbumPlugin(CMSPluginBase):
    """Album CMS plugin."""

    name = _('Album')
    model = pluginmodels.Album
    render_template = 'cmsplugin_photologue_pro/album_plugin.html'

    def render(self, context, instance, placeholder):
        photos = instance.album.photos.all().order_by('id')
        context.update({
            'gallery': instance.album,
            'photos': photos,
        })
        return context

plugin_pool.register_plugin(AlbumPlugin)
