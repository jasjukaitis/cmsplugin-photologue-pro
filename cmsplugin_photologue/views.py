# -*- coding: utf-8 -*-

from django.http import HttpResponse

def overview(request):
    """Shows all available photo galleries."""
    return HttpResponse('')

def album(request, album):
    """Shows all images of album."""
    return HttpResponse('')

def photo(request, album, photo):
    """Shows a detailed view of the photo."""
    return HttpResponse('')
