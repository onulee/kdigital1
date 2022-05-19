from datetime import datetime
from django.db import models

class Member(models.Model):
    m_no = models.AutoField(primary_key=True)
    m_id = models.CharField(max_length=30)
    m_pw = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100)
    m_tel = models.CharField(max_length=13)
    m_zipcode = models.CharField(max_length=5)
    m_address1 = models.CharField(max_length=1000)
    m_address2 = models.CharField(max_length=1000)
    m_date = models.DateTimeField(default=datetime.now(),blank=True)
    
    def __str__(self):
        return self.m_id
    