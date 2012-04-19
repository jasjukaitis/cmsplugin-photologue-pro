# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from photologue import models

def overview(request):
    """Shows all available photo galleries."""
    galleries = models.Gallery.objects.filter(is_public=True)
    return render(request, 'cmsplugin_photologue_pro/index.html',
                  {'galleries': galleries,
                   'order': [1, 2, 3]})

def album(request, album):
    """Shows all images of album."""
    gallery = models.Gallery.objects.get(pk=album)
    photos = gallery.photos.all().order_by('id')
    return render(request, 'cmsplugin_photologue_pro/album.html',
                  {'gallery': gallery,
                   'photos': photos})

def photo(request, album, photo):
    """Shows a detailed view of the photo."""
    gallery = models.Gallery.objects.get(pk=album)
    photo = gallery.photos.get(pk=photo)
    photosize = models.PhotoSize.objects.get(name='normal')
    photo.create_size(photosize)
    exif = None
    previous_photo = photo.get_previous_in_gallery(gallery)
    next_photo = photo.get_next_in_gallery(gallery)
    if getattr(settings, 'PHOTOLOGUE_PRO_EXIF_ENABLED', False):
        exif = photo.EXIF
    photo.view_count += 1
    photo.save()
    return render(request, 'cmsplugin_photologue_pro/photo.html',
                  {'gallery': gallery,
                   'photo': photo,
                   'exif': exif,
                   'previous': previous_photo,
                   'next': next_photo})
