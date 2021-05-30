from django import template

register = template.Library()

@register.inclusion_tag('templatestags/graph.html')
def GraphView():
    return 