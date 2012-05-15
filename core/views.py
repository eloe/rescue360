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
    contentItems = Content.objects.filter(navigationNode__parentNode__id=navigationNode.id).order_by('-createdDate')
    return render_with_context(request, template_name, { 'navigationNode' : navigationNode, 'breadcrumb': None, 'secondaryNavigation' : secondaryNavigation, 'contentItems' : contentItems })
    
def page(request, parent_slug, slug, navigation_node_id, template_name='core/recent-updates.html'):
    navigationNode = NavigationNode.objects.get(id=navigation_node_id)
    secondaryNavigation = NavigationNode.objects.filter(parentNode__id=navigationNode.parentNode.id)
    thirdNavigation = NavigationNode.objects.filter(parentNode__id=navigationNode.id)
    
    fourthNavigation = { }
    for node in thirdNavigation:
        fourthNavigationNodes = NavigationNode.objects.filter(parentNode__id=node.id)
        if len(fourthNavigationNodes) > 0:
            fourthNavigation[node.id] = fourthNavigationNodes
            
    contentItems = Content.objects.filter(navigationNode__parentNode__id=navigationNode.id).order_by('-createdDate')
    return render_with_context(request, template_name, { 'navigationNode' : navigationNode, 'breadcrumb': navigationNode.get_breadcrumb(), 'secondaryNavigation' : secondaryNavigation, 'thirdNavigation' : thirdNavigation, 'fourthNavigation': fourthNavigation, 'contentItems' : contentItems })
    
def content_page(request, parent_slug, secondary_slug, slug, navigation_node_id, template_name='core/page.html'):
    navigationNode = NavigationNode.objects.get(id=navigation_node_id)
    secondaryNavigation = NavigationNode.objects.filter(parentNode__slug=parent_slug)
    thirdNavigation = NavigationNode.objects.filter(parentNode__id=navigationNode.parentNode.id)
    contentItems = Content.objects.filter(navigationNode__id=navigationNode.id).order_by('-createdDate')
    return render_with_context(request, template_name, { 'navigationNode' : navigationNode, 'breadcrumb': navigationNode.get_breadcrumb(), 'secondaryNavigation' : secondaryNavigation, 'thirdNavigation' : thirdNavigation, 'contentItems' : contentItems })
    
def _get_secondary_navigation(slug):
    secondaryNavigation = NavigationNode.objects.filter(parentNode__slug=slug)
    return secondaryNavigation