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
    
class Comment(models.Model):
    # c_no:댓글번호, member:회원아이디, fboard:게시글번호
    # c_pw:댓글비밀번호, c_content:댓글내용, c_date:날짜
    c_no = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
    fboard = models.ForeignKey(Fboard,on_delete=models.CASCADE)
    c_pw = models.CharField(max_length=100,blank=True)
    c_content = models.TextField()
    c_date = models.DateTimeField(default=datetime.now(),blank=True)    
