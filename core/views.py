from random import choice
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
from django.http import Http404
from django.core.urlresolvers import reverse
from hardlycode.util.mixins.helpers import render_with_context
from django.utils.dateformat import format
from core.models import NavigationNode, Content
import datetime

def default(request, template_name='core/default.html'):
    return render_with_context(request, template_name, { })

def top_navigation(request, slug, template_name='core/page.html'):
    navigationNode = NavigationNode.objects.get(slug=slug)
    secondaryNavigation = NavigationNode.objects.filter(parentNode__slug=slug)
    return render_with_context(request, template_name, { 'navigationNode' : navigationNode, 'secondaryNavigation' : secondaryNavigation })
    
def page(request, parent_slug, slug, navigation_node_id, template_name='core/page.html'):
    navigationNode = NavigationNode.objects.get(id=navigation_node_id)
    leftNavigation = NavigationNode.objects.filter(parentNode__id=navigationNode.id)
    secondaryNavigation = NavigationNode.objects.filter(parentNode__id=navigationNode.parentNode.id)
    contentItems = Content.objects.filter(navigationNode__id=navigationNode.id).order_by('-createdDate')
    return render_with_context(request, template_name, { 'navigationNode' : navigationNode, 'secondaryNavigation' : secondaryNavigation, 'leftNavigation' : leftNavigation, 'contentItems' : contentItems })
    
def content_page(request, parent_slug, secondary_slug, slug, navigation_node_id, template_name='core/page.html'):
    navigationNode = NavigationNode.objects.get(id=navigation_node_id)
    leftNavigation = NavigationNode.objects.filter(parentNode__id=navigationNode.parentNode.id)
    secondaryNavigation = NavigationNode.objects.filter(parentNode__slug=parent_slug)
    contentItems = Content.objects.filter(navigationNode__id=navigationNode.id).order_by('-createdDate')
    return render_with_context(request, template_name, { 'navigationNode' : navigationNode, 'secondaryNavigation' : secondaryNavigation, 'leftNavigation' : leftNavigation, 'contentItems' : contentItems })
    
def _get_secondary_navigation(slug):
    secondaryNavigation = NavigationNode.objects.filter(parentNode__slug=slug)
    return secondaryNavigation