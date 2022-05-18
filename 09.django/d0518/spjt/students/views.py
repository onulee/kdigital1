from django.http import HttpResponseRedirect
from django.urls import reverse
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
    s_hobby = request.POST.getlist('hobby')  # hobby list배열형태
    print("s_hobby list : ",s_hobby)
    # db -> list타입 저장안됨.
    # s_hobby list타입 -> str타입변경
    # s_hobby list :  ['게임', '골프', '수영', '독서']
    s_hobby = ','.join(s_hobby)
    print("s_hobby join : ",s_hobby)
    print("s_hobby join타입 : ",type(s_hobby))
    ss_hobby = s_hobby.split(',')
    print('ss_hobby :',ss_hobby)
    print('ss_hobby 타입 :',type(ss_hobby))
    
    
    return HttpResponseRedirect(reverse('index'))