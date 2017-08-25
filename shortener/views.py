# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import View
from django.shortcuts import render,get_object_or_404
from .models import KirrURL
from analytics.models import ClickEvent
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
        context = {
            "form":form
        }
        template = 'shortener/home.html'
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = KirrURL.objects.get_or_create(url =new_url )
            context = {
                "object":obj,
                "created":created
            }
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already-exists.html'

        return render(request,template,context)
class URLRedirectView(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        obj = get_object_or_404(KirrURL,shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
