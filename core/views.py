from random import choice
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.db.models import Q
from hardlycode.util.mixins.helpers import render_with_context
from django.utils.dateformat import format
from core.models import NavigationNode, Content
import datetime

# homepage
def default(request, template_name='core/default.html'):
    contentItems = Content.objects.all().order_by('-createdDate')[:5]
    return render_with_context(request, template_name, { 'contentItems' : contentItems })

# /education
def first_level_page(request, slug, template_name='core/recent-updates.html'):
    navigationNode = NavigationNode.objects.get(slug=slug)
    secondaryNavigation = NavigationNode.objects.filter(parentNode__slug=slug)
    contentItems = Content.objects.filter(
                            Q(navigationNode__parentNode__parentNode__id=navigationNode.id) | Q(navigationNode__parentNode__parentNode__parentNode__id=navigationNode.id)).order_by('-createdDate')[:5]


    return render_with_context(request, template_name, { 'navigationNode' : navigationNode,
                                                            'breadcrumb': None,
                                                            'secondaryNavigation' : secondaryNavigation,
                                                            'contentItems' : contentItems })

# /education/library/4/
def second_level_page(request, parent_slug, slug, navigation_node_id, template_name='core/recent-updates.html'):
    navigationNode = NavigationNode.objects.get(id=navigation_node_id)
    secondaryNavigation = NavigationNode.objects.filter(parentNode__id=navigationNode.parentNode.id)
    thirdNavigation = NavigationNode.objects.filter(parentNode__id=navigationNode.id)

    fourthNavigation = { }
    for node in thirdNavigation:
        fourthNavigationNodes = NavigationNode.objects.filter(parentNode__id=node.id)
        if len(fourthNavigationNodes) > 0:
            fourthNavigation[node.id] = fourthNavigationNodes

    contentItems = Content.objects.filter(
                            Q(navigationNode__parentNode__id=navigationNode.id) | Q(navigationNode__parentNode__parentNode__id=navigationNode.id)).order_by('-createdDate')[:5]
    return render_with_context(request, template_name, { 'navigationNode' : navigationNode,
                                                            'breadcrumb': navigationNode.get_breadcrumb(),
                                                            'secondaryNavigation' : secondaryNavigation,
                                                            'thirdNavigation' : thirdNavigation,
                                                            'fourthNavigation': fourthNavigation,
                                                            'contentItems' : contentItems })

# /education/library/technical-books/9/
def third_level_page(request, parent_slug, secondary_slug, slug, navigation_node_id, template_name='core/page.html'):
    navigationNode = NavigationNode.objects.get(id=navigation_node_id)
    secondaryNavigation = NavigationNode.objects.filter(parentNode__slug=parent_slug)
    thirdNavigation = NavigationNode.objects.filter(parentNode__id=navigationNode.parentNode.id)
    contentItems = Content.objects.filter(Q(navigationNode__id=navigationNode.id) | Q(navigationNode__parentNode__id=navigationNode.id)).order_by('-createdDate')
    return render_with_context(request, template_name, { 'navigationNode' : navigationNode,
                                                            'breadcrumb': navigationNode.get_breadcrumb(),
                                                            'secondaryNavigation' : secondaryNavigation,
                                                            'thirdNavigation' : thirdNavigation,
                                                            'contentItems' : contentItems })

# /education/library/technical-books/confined-space/22/
def fourth_level_page(request, parent_slug, secondary_slug, third_slug, slug, navigation_node_id, template_name='core/page.html'):
    navigationNode = NavigationNode.objects.get(id=navigation_node_id)
    secondaryNavigation = NavigationNode.objects.filter(parentNode__slug=parent_slug)
    thirdNavigation = NavigationNode.objects.filter(parentNode__slug=secondary_slug)
    contentItems = Content.objects.filter(navigationNode__id=navigationNode.id).order_by('-createdDate')
    return render_with_context(request, template_name, { 'navigationNode' : navigationNode,
                                                            'breadcrumb': navigationNode.get_breadcrumb(),
                                                            'secondaryNavigation' : secondaryNavigation,
                                                            'thirdNavigation' : thirdNavigation,
                                                            'contentItems' : contentItems })

def _get_secondary_navigation(slug):
    secondaryNavigation = NavigationNode.objects.filter(parentNode__slug=slug)
    return secondaryNavigation