# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shortener.models import KirrURL
# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self,instance):
        if isinstance(KirrURl,instance):
            obj,created = seld.objects.get_or_create(kirr_url = instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    kirr_url = models.OneToOneField(KirrURL)
    count = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now_add =True )
    updated = models.DateTimeField(auto_now =True )

    objects = ClickEventManager()
    
    def __str__(self):
        return str(self.count)
