# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import View
from django.shortcuts import render,get_object_or_404
from .models import KirrURL
# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'shortener/home.html',{})

class KirrCBView(View):
    def get(self,request,*args,**kwargs):
        obj = get_object_or_404(KirrURL,shortcode = shortcode)
        return HttpResponseRedirect(obj.url)
