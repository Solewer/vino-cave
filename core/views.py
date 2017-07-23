# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Vin


def youhou(request):
    return HttpResponse("Youhou !!")

def rajeunir(request):
    v=Vin.objects.all()[0]
    v.year = v.year+1
    v.save()
    return HttpResponse("Premier vin : {}".format(v))
    #return HttpResponse("Index : {} vin(s)".format(Vin.objects.count()))

def index(request):
    liste_vins = Vin.objects.all()
    context = {'liste_vins': liste_vins}
    return render(request, 'index.html', context)

def liste(request):
    return HttpResponse("Liste : "+", ".join([unicode(v) for v in Vin.objects.all()]))
