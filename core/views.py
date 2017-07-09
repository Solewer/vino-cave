# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def youhou(request):
    return HttpResponse("Youhou !!")

def index(request):
    return HttpResponse("Index")

def liste(request):
    return HttpResponse("Liste")
