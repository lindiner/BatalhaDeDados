from django import template

register = template.Library()

@register.inclusion_tag('templatestags/graph.html')
def GraphView():
    return 

@register.inclusion_tag('templatestags/graph_aluno1.html')
def GraphView1():
    return 
