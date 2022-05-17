from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student

# 학생등록페이지
def stuWrite(request):
    # request.method확인으로 함수사용
    if request.method == 'GET':
        return render(request,'stuWrite.html')
    else:
        # form데이터 - POST
        name = request.POST.get('name') 
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')
        print('form name : ',name)            
        # db저장
        Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
        # qs = Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
        # qs.save()
                    
        return HttpResponseRedirect(reverse('index'))    
 
# 학생전체리스트
def stuList(request):
    qs = Student.objects.order_by('s_name')
    count = qs.count()
    # dic타입으로 저장
    context = {'stuList':qs,"stuCount":count}
    # context데이터를 html에 보냄
    return render(request,'stuList.html',context)   

# 학생상세페이지 - 간단url:매개변수만 가능, 파라미터:request.GET.get만 가능
def stuView(request,name,major):
    # name = request.GET.get('name')
    # name변수를 가지고 학생 검색 - 타입 : Student객체
    qs = Student.objects.get(s_name=name)
    context={'stu':qs}
    return render(request,'stuView.html',context)
    






#### stuWrite, stuWriteOk함수를 분리해서 사용

# # 학생 db 등록 - form데이터 전달받음 : name,major,age,grade,gender
# def stuWriteOk(request):
#     # form데이터 - POST
#     name = request.POST.get('name') 
#     major = request.POST.get('major')
#     age = request.POST.get('age')
#     grade = request.POST.get('grade')
#     gender = request.POST.get('gender')
#     print('form name : ',name)            
#     # db저장
#     Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
#     # qs = Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
#     # qs.save()
                
#     return HttpResponseRedirect(reverse('index'))


#######  db 명령어 #######
# # 1. create
# # query = Student(s_name='홍길순',s_major='영문학과',s_age=24,s_grade=4,s_gender='여자')
# # query.save()  

# # 2. read  
# # 전체데이터 읽어오기
# qs = Student.objects.all()
# print(qs)
# # 1개데이터 읽어오기
# qs2 = Student.objects.get(s_name='홍길동')
# print(qs2)
# # 검색
# qs3 = Student.objects.filter(s_name__contains='홍')
# print(qs3)

# # 3. update
# qs4 = Student.objects.get(s_name='홍길동')
# qs4.s_major = '아동학과'
# qs4.save()
# print('변경되었습니다')

# # 4. delete
# # qs5 = Student.objects.get(s_name='홍길자')
# # qs5.delete()
# # print('삭제되었습니다.')