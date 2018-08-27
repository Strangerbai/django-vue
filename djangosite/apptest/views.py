# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# Create your views here.
def welcome(request):
    # return HttpResponse("<h1>Welcome to my app</h1>")
    return JsonResponse({"result": 0, "msg": "执行成功"})

