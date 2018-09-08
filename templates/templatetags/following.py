from django import template
from users.models import User

register = template.Library()

@register.simple_tag(takes_context=True)

def followingBool(context, key):
    user = context.get('user')
    query = User.objects.filter(username=user)[0].following.filter(pk=key).exists()
    
    if query:
        return 'Seguindo'
    else:
        return 'Seguir'
        