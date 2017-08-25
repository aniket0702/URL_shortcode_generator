# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shortener.models import KirrURL
# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self,kirrinstance):
        if isinstance(kirrinstance,KirrURL):
            obj, created = self.get_or_create(kirr_url = kirrinstance)
            obj.count += 1
            obj.save()
            print(obj.count)
            return obj.count
        return None


class ClickEvent(models.Model):
    kirr_url = models.OneToOneField(KirrURL)
    count = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now_add =True )
    updated = models.DateTimeField(auto_now =True )

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i = self.count)
