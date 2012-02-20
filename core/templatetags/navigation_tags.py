import re
from django import template
from django.template import Library, Node, TemplateSyntaxError
from django.core.urlresolvers import reverse, get_resolver
from core.models import NavigationNode

register = template.Library()

@register.tag(name="get_top_navigation")
def get_top_navigation(parser, token):
    try:
        bits = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError(_('tag requires exactly two arguments'))
    if bits[1] != 'as':
        raise TemplateSyntaxError(_("first argument to tag must be 'as'"))
    return TopNavigationNode(bits[2])
        
class TopNavigationNode(Node):
    """
    Get the top navigation and add to the context
    """
    def __init__(self, context_var):
        self.context_var = context_var
 
    def render(self, context):
        context[self.context_var] = NavigationNode.objects.filter(parentNode=None).order_by('-id')
        return ''