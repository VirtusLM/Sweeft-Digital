from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from random import choices
from string import ascii_letters, digits

from .models import URL



def shortener():
    url_length = 7 
    random_chars = ascii_letters + digits

    # Generate a random string of length 7
    short_url = ''.join(choices(random_chars, k=url_length))
    
    # Checks if short_url id exists
    if URL.objects.filter(short_url=short_url).exists():
        shortener()
    return short_url


def redirect_url(request, short):
    try:
        urlshort = URL.objects.get(short_url=short)
        urlshort.click_times += 1        
        urlshort.save()
        return HttpResponseRedirect(urlshort.long_url)
    except:
        raise Http404


def home(request):
    items = URL.objects.all()
    return render(request, 'urlshortener/home.html', {'urls': items})



