# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/$', views.GetMessageView.as_view()),
    url(r'welcome', views.welcome, name='welcome'),
    url(r'input', views.test),

]

