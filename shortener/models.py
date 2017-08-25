# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .utils import code_generator,create_shortcode
from django.db import models
from django.conf import settings

# 15 = getattr(settings, "15",15)

class KirrURLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_main = super(KirrURLManager,self).all(*args,**kwargs)
        qs = qs_main.filter(active=True)
        return qs
    def refresh_shortcode(self,items=0):
        qs = KirrURL.objects.filter(id__gte = 1)   #greater_and_equal to = id__gte
        if items is not None and isinstance(items,int):
            qs = qs.order_by('-id')[:items]
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_code+=1
            print q.shortcode
        return new_code
# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length= 220 )
    shortcode = models.CharField(max_length = 15,unique = True,blank = True)
    timestamp = models.DateTimeField(auto_now_add =True )#when the field was created
    updated = models.DateTimeField(auto_now =True )#when the field was last created
    active  = models.BooleanField(default = True)


    objects = KirrURLManager()
    some_random = KirrURLManager

    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL,self).save(*args,**kwargs)
    def __str__(self):
        return (str(self.url))
    def __unicode__(self):
        return (str(self.url))

    def get_short_url(self):
        return "mysite.com:8000/{shortcode}".format(shortcode = self.shortcode)
