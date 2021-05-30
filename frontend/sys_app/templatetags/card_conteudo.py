from django import template

register = template.Library()

@register.inclusion_tag('templatestags/card_conteudo.html')
def card_conteudo(context):
    return {'context':context}