from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '/static/img/photo.png'

@register.simple_tag()
def media_tag(val):
    if val:
        return f'/media/{val}'
    return '/static/img/photo.png'