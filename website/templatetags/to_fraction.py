from django import template
import math

register = template.Library()

@register.filter(name='to_fraction')
def to_fraction(value):
  rounded = math.floor(value)
  remainder = value % 1
  ratio = remainder.as_integer_ratio()

  if (rounded == 0):
    return f'<span class="vfrac"><sup>{ratio[0]}</sup>&frasl;<sub>{ratio[1]}</sub></span>'
  
  return f'{rounded}<span class="vfrac"><sup>{ratio[0]}</sup>&frasl;<sub>{ratio[1]}</sub></span>'