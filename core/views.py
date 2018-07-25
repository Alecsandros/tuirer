from django.shortcuts import render
from django.http import HttpResponse
from .helpers import get_character_name, ip_info

def index(request):
    country = ip_info('country_name')
    flag = ip_info('flag')
    flag_image = f'<img src="{flag}" width="120" />'
    return HttpResponse(f'Olá do <b> {country}</b>!<br>{flag_image}')

