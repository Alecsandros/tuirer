from django.shortcuts import render
from django.http import HttpResponse
from .helpers import get_character_name, ip_info
from datetime import datetime

def index(request):
    context = {
        'now': datetime.now()
    }
    return render(request, 'index.html', context)

