from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CompileInfo(models.Model):
    pro_id = models.CharField(max_length=20)
    pro_lang = models.TextField(null=True)
    status = models.IntegerField(null=True)
    error_result = models.TextField(null=True)
    out_result = models.TextField(null=True)


