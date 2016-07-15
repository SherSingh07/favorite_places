from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    """
    model for category for a place

    we will be storing places in category,
    eg. travel, shopping, work, party etc.
    """
    user = models.ForeignKey(User)	
    title = models.CharField(max_length=128, verbose_name=_('Title'))
    description = models.CharField(max_length=1024, verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __unicode__(self):
        """
        function returns unicode representation of category
        """
        return "%s" % self.title


class Place(models.Model):
    """
    model for user places
    """
    user = models.ForeignKey(User)	
    category = models.ForeignKey(Category)	
    img = models.FileField(upload_to = 'photos/')
    lat = models.DecimalField(max_digits=12, decimal_places=6)
    lng = models.DecimalField(max_digits=12, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    
    def __unicode__(self):
        """
        function returns unicode representation of place
        """
        return "%s" % self.img
