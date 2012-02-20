from django.db import models
from hardlycode.util.mixins.models import SlugMixin, ImageMixin

class NavigationNode(SlugMixin):
    name = models.CharField(max_length=50)
    adminName = models.CharField(max_length=50)
    parentNode = models.ForeignKey('NavigationNode', blank=True, null=True)
    allowContent = models.BooleanField()
    hide = models.BooleanField()
    createdDate = models.DateTimeField(auto_now_add=True)
    slugValue = 'name'

    class Meta:
        ordering = ('createdDate',)
        verbose_name_plural = 'Navigation Nodes'

    def __unicode__(self):
        return u"%s" % self.adminName
        
class Content(ImageMixin):
    navigationNode = models.ForeignKey('NavigationNode')
    name = models.CharField(max_length=50)
    subtext = models.CharField(max_length=50,blank=True)
    description = models.TextField()
    externalURL = models.URLField()
    hide = models.BooleanField()
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    slugValue = 'name'
    
    class Meta:
        ordering = ('createdDate',)
        
    def __unicode__(self):
        return u"%s" % self.name