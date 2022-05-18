from django.contrib import admin
from students.models import Student

# admin페이지에서 컬럼을 추가하는 방법
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_no','s_name','s_major','s_age','s_grade']

# admin.site.register(Student,StudentAdmin)
