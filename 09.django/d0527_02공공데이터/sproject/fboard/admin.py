from django.contrib import admin
from fboard.models import Fboard,Comment

@admin.register(Fboard)
class FboardAdmin(admin.ModelAdmin):
    list_display = ['f_no','member','f_title','f_updatedate']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['c_no','member','fboard','c_content','c_date']