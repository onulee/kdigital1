from datetime import datetime
from django.db import models

class Freeboard(models.Model):
    f_no = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100)
    f_title = models.CharField(max_length=1000)
    f_content = models.TextField()
    f_group = models.IntegerField()
    f_step = models.IntegerField()
    f_indent = models.IntegerField()
    f_hit = models.IntegerField(default=1)
    f_createdate =models.DateTimeField(default=datetime.now(),blank=True)
    f_updatedate = models.DateTimeField(default=datetime.now(),blank=True)
    f_file = models.ImageField(blank=True)
    
    def __str__(self):
        return self.f_title
    
