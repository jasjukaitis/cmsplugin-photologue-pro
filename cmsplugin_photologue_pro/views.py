# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from photologue import models

def overview(request):
    """Shows all available photo galleries."""
    galleries = models.Gallery.objects.select_related()
    galleries = galleries.order_by('title').filter(is_public=True)
    for gallery in galleries:
        photos = gallery.photos.filter(is_public=True).order_by('id')[:3]
        gallery.filtered_photos = photos
    return render(request, 'cmsplugin_photologue_pro/index.html',
                  {'galleries': galleries,
                   'order': [1, 2, 3]})

def album(request, album):
    """Shows all images of album."""
    tpl = 'cmsplugin_photologue_pro/album.html'
    try:
        gallery = models.Gallery.objects.get(pk=album)
    except models.Gallery.DoesNotExist:
        return render(request, tpl)
    if not gallery.is_public:
        return render(request, tpl,
                      {'is_not_public': True})
    photos = gallery.photos.filter(is_public=True).order_by('id')
    return render(request, tpl,
                  {'gallery': gallery,
                   'photos': photos})

def photo(request, album, photo):
    """Shows a detailed view of the photo."""
    tpl = 'cmsplugin_photologue_pro/photo.html'
    try:
        gallery = models.Gallery.objects.get(pk=album)
    except models.Gallery.DoesNotExist:
        return render(request, tpl)
    try:
        photo = gallery.photos.get(pk=photo)
    except models.Photo.DoesNotExist:
        return render(request, tpl)
    if not gallery.is_public or not photo.is_public:
        return render(request, tpl, {'is_not_public': True})
    photosize = models.PhotoSize.objects.get(name='normal')
    photo.create_size(photosize)
    exif = None
    previous_photo = photo.get_previous_in_gallery(gallery)
    next_photo = photo.get_next_in_gallery(gallery)
    if getattr(settings, 'PHOTOLOGUE_PRO_EXIF_ENABLED', False):
        exif = photo.EXIF
    return render(request, tpl,
                  {'gallery': gallery,
                   'photo': photo,
                   'exif': exif,
                   'previous': previous_photo,
                   'next': next_photo})
