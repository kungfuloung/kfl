from django import template
register = template.Library()

@register.filter
def is_member_of(element, list):
	return element in list

# Create your tests here.
