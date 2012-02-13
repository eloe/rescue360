from django.contrib import admin
from django import forms
from core.models import NavigationNode, Content

class NavigationNodeAdmin(admin.ModelAdmin):
	fieldsets = [
	    ('Information', {'fields': ['name', 'adminName', 'parentNode', 'allowContent', 'hide']}),
	]
	ordering = ('createdDate',)
	list_display = ('adminName', 'parentNode', 'hide', 'allowContent')
	list_filter = ['createdDate']
	date_hierarchy = 'createdDate'
	
class ContentAdmin(admin.ModelAdmin):
	fieldsets = [
	    ('Information', {'fields': ['name', 'navigationNode', 'hide', 'externalURL', 'description']}),
	]
	ordering = ('createdDate', 'lastModified',)
	list_display = ('name', 'navigationNode', 'hide')
	list_filter = ['createdDate', 'lastModified']
	date_hierarchy = 'createdDate'
	
admin.site.register(NavigationNode, NavigationNodeAdmin)
admin.site.register(Content, ContentAdmin)