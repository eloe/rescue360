from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'epio_skel.views.home', name='home'),
    # url(r'^epio_skel/', include('epio_skel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
	(r'^$', 'core.views.default'),
    (r'^(?P<parent_slug>.+)/(?P<secondary_slug>.+)/(?P<third_slug>.+)/(?P<slug>.+)/(?P<navigation_node_id>.+)/$', 'core.views.fourth_level_page'),    
    (r'^(?P<parent_slug>.+)/(?P<secondary_slug>.+)/(?P<slug>.+)/(?P<navigation_node_id>.+)/$', 'core.views.third_level_page'),
    (r'^(?P<parent_slug>.+)/(?P<slug>.+)/(?P<navigation_node_id>.+)/$', 'core.views.second_level_page'),
	(r'^(?P<slug>.+)/$', 'core.views.first_level_page'),
)