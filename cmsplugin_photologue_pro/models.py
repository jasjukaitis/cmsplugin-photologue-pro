# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

PHOTOS_PER_PAGE = (
    (10, 10),
    (25, 25),
    (50, 50),
    (100, 100),
    (250, 250),
)

class Album(CMSPlugin):
    """Model for Album CMS plugin."""

    album = models.ForeignKey('photologue.Gallery', verbose_name=_('Album'))
    per_page = models.IntegerField(_('Photos per page'),
                                   choices=PHOTOS_PER_PAGE, default=100,
                                   max_length=3)
