from django.contrib import admin
from member.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ['m_no','m_name','m_id']
    
admin.site.register(Member,MemberAdmin)