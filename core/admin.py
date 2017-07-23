# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Vin, Bouteille

admin.site.register(Vin)
admin.site.register(Bouteille)
