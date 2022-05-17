from django.contrib import admin
# students > models 연결
from students.models import Student

# Student 객체를 출력하면 __str__출력됨.
# admin.site.register(Student)

# admin컬럼이 3개가 노출됨.
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['s_name','s_major','s_age']
# admin.site.register(Student,StudentAdmin)    

# @사용 - decorator 사용
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_name','s_major']
    