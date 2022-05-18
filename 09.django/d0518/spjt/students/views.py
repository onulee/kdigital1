from django.shortcuts import render
from students.models import Student

# 학생등록함수
def stuWrite(request):
    return render(request,'stuWrite.html')

# 학생등록저장함수
def stuWriteOk(request):
    s_name = request.POST.get('name') # data 넘어오지 않으면 none
    # s_name = request.POST['name'] - data 넘어오지 않으면 error
    s_major = request.POST.get('major')
    s_age = request.POST.get('age')
    s_grade = request.POST.get('grade')
    s_gender = request.POST.get('gender')
    s_hobby = request.POST.getlist('hobby')  # hobby배열형태
    
    return 