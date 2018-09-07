from django import template
from tuites.models import Tuite

register = template.Library()

@register.simple_tag
def tuitesPostOrder():
    tuites = Tuite.objects.all().order_by('-date_created')
    return tuites