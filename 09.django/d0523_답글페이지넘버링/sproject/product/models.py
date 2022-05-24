from datetime import datetime
from django.db import models
from member.models import Member

class Product(models.Model):
    p_no = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_servings = models.CharField(max_length=100,default='2인분')
    p_unitPrice = models.IntegerField(default=0)
    p_description = models.TextField()
    p_category = models.CharField(max_length=20,default='요리')
    p_manufacturer = models.CharField(max_length=20,default='CJONE')
    p_unit = models.IntegerField(default=100)
    p_fileName = models.ImageField(blank=True)
    # p_createdate =models.DateTimeField(default=datetime.now(),blank=True)
    # p_updatedate = models.DateTimeField(default=datetime.now(),blank=True)
    
    def __str__(self):
        return self.p_name


