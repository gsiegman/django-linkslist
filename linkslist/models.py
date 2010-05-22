from django.db import models
from imagekit.models import ImageModel

class LinksList(models.Model):
    key = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=75)
    
    objects = models.Manager()
    
    class Meta:
        ordering = ('title',)
    
    def __unicode__(self):
        return '%s links list' % self.title

class LinksListItemImage(ImageModel):
    name = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to='photos')
    caption = models.TextField()
    num_views = models.PositiveIntegerField(editable=False,
        default=0
    )
    
    class IKOptions:
        spec_module = 'linkslist.specs'
        image_field = 'original_image'
        save_count_as = 'num_views'
        
    def __unicode__(self):
        return self.name

class LinksListItem(models.Model):
    links_list = models.ForeignKey(LinksList)
    image = models.ForeignKey(LinksListItemImage, blank=True, null=True)
    link = models.URLField(verify_exists=False)
    description = models.CharField(max_length=160, blank=True)
    order = models.PositiveSmallIntegerField()
    
    class Meta:
        unique_together = (('links_list', 'order',),)
        ordering = ['order']
    
    def __unicode__(self):
        return 'Links list item #%s for %s' % (self.order, self.links_list,)