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

    def get_absolute_url(self):
        breadcrumb = self.get_breadcrumb()

        url = "/"

        for crumb in breadcrumb:
            url += "%s/" % crumb.slug

        if len(breadcrumb) > 1:
            url += "%i/" % self.id

        return url


    def get_breadcrumb(self):
        array = []
        self._get_breadcrumb_child(array)

        nodes = []
        for node in array:
            if node:
                nodes.append(node)

        return nodes

    def _get_breadcrumb_child(self, array):
        array.insert(0, self)
        if self.parentNode:
            array.append(self.parentNode._get_breadcrumb_child(array))

    def _get_children(self):
        return NavigationNode.objects.filter(parentNode__id=self.id)

    childNodes = property(_get_children)

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