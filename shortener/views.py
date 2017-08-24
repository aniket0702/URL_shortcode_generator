# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import View
from django.shortcuts import render,get_object_or_404
from .models import KirrURL
from .forms import SubmitUrlForm
# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        form = SubmitUrlForm()
        context = {
            "form":form
        }
        return render(request,'shortener/home.html',context)
    def post(self,request,*args,**kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['url'])
        context = {
            "form":form
        }
        return render(request,'shortener/home.html',context)
class KirrCBView(View):
    def get(self,request,*args,**kwargs):
        obj = get_object_or_404(KirrURL,shortcode = shortcode)
        return HttpResponseRedirect(obj.url)
