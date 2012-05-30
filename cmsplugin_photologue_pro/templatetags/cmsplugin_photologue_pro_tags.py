from datetime import datetime
from django import template
from django.utils import formats
from photologue import models

register = template.Library()

@register.inclusion_tag('cmsplugin_photologue_pro/polaroid.html')
def polaroid_thumbnail(photo, photosize=None, counter=''):
    if not photosize:
        photosize = models.PhotoSize.objects.get(name='thumbnail')
    photo.create_size(photosize)
    return {
        'url': photo.get_thumbnail_url,
        'title': photo.title,
        'counter': counter,
    }

@register.simple_tag
def exif(photo, attr):
    value = str(photo.EXIF.get(attr, ''))
    if attr == 'EXIF DateTimeOriginal':
        dt = datetime.strptime(str(value), '%Y:%m:%d %H:%M:%S')
        value = formats.date_format(dt, 'DATETIME_FORMAT', True)
    elif attr == 'EXIF ApertureValue':
        f = value.split('/')
        if len(f) == 1:
            aperture = float(f[0])
        else:
            aperture = float(f[0]) / float(f[1])
        value = 'f/%.1f' % aperture
    return value
