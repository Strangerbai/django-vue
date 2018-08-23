# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your models here.
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20,null=True)
    content = models.CharField(max_length=200,null=True)
    kind = models.CharField(max_length=20,null=True)