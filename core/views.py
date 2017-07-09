# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Vin


def youhou(request):
    return HttpResponse("Youhou !!")

def index(request):
    return HttpResponse("Index : {} vin(s)".format(Vin.objects.count()))

def liste(request):
    return HttpResponse("Liste : "+", ".join([unicode(v) for v in Vin.objects.all()]))
