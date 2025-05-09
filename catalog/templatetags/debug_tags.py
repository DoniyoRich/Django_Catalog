from django import template

register = template.Library()

@register.simple_tag
def debug_object(obj):
    return dir(obj)