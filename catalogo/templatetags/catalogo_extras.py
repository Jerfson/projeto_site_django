from django import template

register = template.Library()


@register.filter
def brl(value):
    """Formata um Decimal ou float como moeda brasileira: R$ 1.500,00"""
    try:
        value = float(value)
    except (TypeError, ValueError):
        return value
    formatted = f'{value:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return f'R$ {formatted}'
