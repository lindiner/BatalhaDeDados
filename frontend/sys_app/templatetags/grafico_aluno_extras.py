from django import template

register = template.Library()

@register.inclusion_tag('templatestags/graph_aluno.html')
def GraphView():
    return 


