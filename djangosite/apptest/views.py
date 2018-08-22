# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse("<h1>Welcome to my app</h1>")

