# -*- coding: utf-8 -*-
from django.db import models

from cms.models import CMSPlugin

class Album(CMSPlugin):
    """Model for Album CMS plugin."""

    album = models.ForeignKey('photologue.Gallery')
