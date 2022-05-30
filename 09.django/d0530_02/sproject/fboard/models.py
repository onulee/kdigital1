from datetime import datetime
from django.db import models
from member.models import Member

class Fboard(models.Model):
    f_no = models.AutoField(primary_key=True)
    # primary key:Member객체, id 1개 컬럼으로 받는데, ForeignKey:Member객체
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
    # id = models.CharField(max_length=100)
    f_title = models.CharField(max_length=1000)
    f_content = models.TextField()
    f_group = models.IntegerField(default=0)
    f_step = models.IntegerField(default=0)
    f_indent = models.IntegerField(default=0)
    f_hit = models.IntegerField(default=1)
    f_createdate =models.DateTimeField(default=datetime.now(),blank=True)
    f_updatedate = models.DateTimeField(default=datetime.now(),blank=True)
    f_file = models.ImageField(blank=True)
    
    def __str__(self):
        return self.f_title
