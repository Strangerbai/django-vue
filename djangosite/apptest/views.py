# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# from rest_framework.views import APIView
# from django.http import JsonResponse
#
# # Create your views here.
# class GetMessageView(APIView):
#     # get 请求
#     def get(self, request):
#         # 获取参数数据
#         get = request.GET
#         # 获取参数 a
#         a = get.get('a')
#         print(a)
#         # 返回信息
#         d = {
#             'status': 1,
#             'message': 'success',
#             }
#         return JsonResponse(d)

import os
from forms import  Test
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

def test(request):
    if request.method == 'POST':
        form = Test(request)
