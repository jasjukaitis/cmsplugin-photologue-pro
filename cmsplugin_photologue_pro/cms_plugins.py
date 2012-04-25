# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.core.paginator import EmptyPage, InvalidPage, Paginator
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
        if not instance.album.is_public:
            context.update({'is_not_public': True})
            return context
        photo_instance = instance.album.photos.filter(is_public=True)
        photo_instance = photo_instance.order_by('id')
        per_page = instance.per_page or 100
        paginator = Paginator(photo_instance, per_page)
        try:
            page = max(int(context.get('request', 1).GET.get('page', 1)))
        except (ValueError, TypeError):
            page = 1
        try:
            photos = paginator.page(page)
        except (EmptyPage, InvalidPage):
            photos = paginator.page(paginator.num_pages)
        context.update({
            'gallery': instance.album,
            'photos': photos,
            'pages': paginator.page_range,
            'current_page': page,
        })
        return context

plugin_pool.register_plugin(AlbumPlugin)
