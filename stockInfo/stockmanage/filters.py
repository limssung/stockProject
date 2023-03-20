from django import template

register = template.Library()

@register.filter()
def ranges(count=180):
    return range(0, count)