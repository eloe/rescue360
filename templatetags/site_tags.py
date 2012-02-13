from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy
from django.conf import settings
from django import template
from hardlycode.util.mixins.helpers import VariableNode, VariableTag

register = template.Library()

@register.simple_tag
def site_name():
	try:
		return ugettext_lazy(Site.objects.get_current().name)
	except Site.DoesNotExist:
		return None

@register.simple_tag
def site_domain():
	try:
		return Site.objects.get_current().domain
	except Site.DoesNotExist:
		return None

@register.simple_tag
def site_version():
	return "v=" + str(settings.VERSION)
register.simple_tag(site_version)

class ModuloNode(template.Node):
	def __init__(self, var1, var2):
		self.var1, self.var2 = var1, var2

	def __repr__(self):
		return "<ModuloNode>"

	def render(self, context):
		try:
			val1 = template.resolve_variable(self.var1, context)
		except template.VariableDoesNotExist:
			val1 = None
		try:
			val2 = template.resolve_variable(self.var2, context)
		except template.VariableDoesNotExist:
			val2 = None

		return val1 % val2
 
def do_mod(parser, token,):
	bits = list(token.split_contents())
	if len(bits) != 3:
		raise template.TemplateSyntaxError, "%r takes two arguments" % bits[0]

	return ModuloNode(bits[1], bits[2])
 
def mod(parser, token):
  return do_mod(parser, token)
 
register.tag('mod', mod)

class RowNode(template.Node):
	def __init__(self, perRow, itemNum):
		self.perRow, self.itemNum = perRow, itemNum

	def __repr__(self):
		return "<RowNode>"

	def render(self, context):
		try:
			perRow = template.resolve_variable(self.perRow, context)
		except template.VariableDoesNotExist:
			perRow = None

		try:
			itemNum = template.resolve_variable(self.itemNum, context)
		except template.VariableDoesNotExist:
			itemNum = None
		
		return int((itemNum / perRow) + 1)
 
def do_row_number(parser, token,):
	bits = list(token.split_contents())
	if len(bits) != 3:
		raise template.TemplateSyntaxError, "%r takes two arguments" % bits[0]

	return RowNode(bits[1], bits[2])
 
def row_number(parser, token):
  return do_row_number(parser, token)
 
register.tag('row_number', row_number)

