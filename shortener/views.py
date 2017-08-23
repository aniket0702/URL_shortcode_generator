# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render,get_object_or_404
from .models import KirrURL
# Create your views here.
def  kirr_redirect_view(request,shortcode = None):
    obj = get_object_or_404(KirrURL,shortcode=shortcode)
    obj_url = obj.url
    # qs = KirrURL.objects.filter(shortcode__iexact = shortcode)
    # if qs.exists() and qs.count()==1:
    #     obj = qs.first()
    #     obj_url = obj.url

    return HttpResponse("Hello"+str(obj_url))

class KirrCBView(View):
    def get(self,request,shortcode = None):
        return HttpResponse("Hello Again"+str(shortcode))
