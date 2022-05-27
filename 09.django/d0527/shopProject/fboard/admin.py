from django.contrib import admin
from fboard.models import Fboard

@admin.register(Fboard)
class FboardAdmin(admin.ModelAdmin):
    list_display = ['f_no','f_title','member','f_updatedate' ]

# admin.site.register(Fboard)