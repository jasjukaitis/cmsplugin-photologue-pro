# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

from photologue.models import Gallery


class AlbumSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Gallery.objects.filter(is_public=True)

    def lastmod(self, obj):
        return obj.date_added

    def location(self, obj):
        return reverse('photologue_album', kwargs={'album': obj.pk})
