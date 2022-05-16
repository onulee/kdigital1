from django.db import models

# Student클래스 선언
class Student(models.Model):
    # s_name varchar2(100) 
    s_name = models.CharField(max_length=100) # 문자(varchar2)
    s_major = models.CharField(max_length=100)
    s_age = models.IntegerField(default=0)   # 정수
    s_grade = models.IntegerField(default=0) # 정수
    s_gender = models.CharField(max_length=3) # 문자
    
    def __str__(self):
        return self.s_name