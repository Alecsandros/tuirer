from django import template

register = template.Library()

@register.simple_tag(takes_context=True)

def liked_tuite_heart_icon(context):
    user = context.get('user')
    tuite = context.get('tuite')

    if(user.is_authenticated):
        if user.liked_tuites.filter(id__in=[tuite.id]).exists():
            return "fas fa-heart" 
    
    return "far fa-heart"
        