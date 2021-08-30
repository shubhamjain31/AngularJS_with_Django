from django import template

register = template.Library()

@register.filter(name="counter")
def counter(value):
	print(value,'sdjjdj')
	value = int(value) + 1
	return value