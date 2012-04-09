from django import template

from photologue import models

register = template.Library()

@register.inclusion_tag('cmsplugin_photologue_pro/polaroid.html')
def polaroid_thumbnail(photo, counter=''):
    photosize = models.PhotoSize.objects.get(name='thumbnail')
    photo.create_size(photosize)
    return {
        'url': photo.get_thumbnail_url,
        'title': photo.title,
        'counter': counter,
    }

@register.simple_tag
def exif(photo, attr):
    return photo.EXIF.get(attr, '')
