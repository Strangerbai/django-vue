# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.
class GetMessageView(APIView):
    # get 请求
    def get(self, request):
        # 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('a')
        print(a)
        # 返回信息
        d = {
            'status': str(a),
            'message': 'success',
            }
        return JsonResponse(d)

import os
from forms import MomnetForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
#
def welcome(request):
    return HttpResponse("<h1>welcome to my tiny app</h1>")
#
@csrf_protect
def test(request):
    if request.method == 'POST':
        form = MomnetForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("welcome"))
    else:
        form = MomnetForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'apptest/templates', 'test_input.html'), {'form':form})


