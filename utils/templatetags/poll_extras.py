from django import template

register = template.Library()

@register.filter(name='dir')
def _dir(_class):
    print(dir(_class))