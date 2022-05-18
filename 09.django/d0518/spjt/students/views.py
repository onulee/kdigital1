from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from students.models import Student

# 학생전체리스트 함수
def stuList(request):
    # db전체데이터 가져오기 - order_by:정렬, -역순정렬
    qs = Student.objects.order_by('-s_no')
    count = qs.count() # 학생전체리스트 개수
    context = {'stuList':qs,'count':count}
    return render(request,'stuList.html',context)

# 학생등록함수
def stuWrite(request):
    return render(request,'stuWrite.html')

# 학생등록저장함수
def stuWriteOk(request):
    name = request.POST.get('name') # data 넘어오지 않으면 none
    # s_name = request.POST['name'] - data 넘어오지 않으면 error
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')  # hobby list배열형태
    print("s_hobby list : ",hobby)
    # db -> list타입 저장안되어서 str변경해야 함.
    # s_hobby list :  ['게임', '골프', '수영', '독서']
    hobby = ','.join(hobby) # list타입 -> str타입변경
    # ss_hobby = s_hobby.split(',') # str타입 -> list타입변경
    
    # db에 저장 -> sqlite3 table insert명령어
    Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender,s_hobby=hobby)
    # qs = Student(s_name=name,s_major=major,s_age=age,s_gender=gender,s_hobby=hobby)
    # qs.save()
    print("insert OK!")
    
    return HttpResponseRedirect(reverse('students:stuList'))