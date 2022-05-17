from django.shortcuts import render
from students.models import Student

def stuWrite(request):
    # 1. create
    # query = Student(s_name='홍길순',s_major='영문학과',s_age=24,s_grade=4,s_gender='여자')
    # query.save()  
    
    # 2. read  
    # 전체데이터 읽어오기
    qs = Student.objects.all()
    print(qs)
    # 1개데이터 읽어오기
    qs2 = Student.objects.get(s_name='홍길동')
    print(qs2)
    # 검색
    qs3 = Student.objects.filter(s_name__contains='홍')
    print(qs3)
    
    # 3. update
    qs4 = Student.objects.get(s_name='홍길동')
    qs4.s_major = '아동학과'
    qs4.save()
    print('변경되었습니다')
    
    # 4. delete
    # qs5 = Student.objects.get(s_name='홍길자')
    # qs5.delete()
    # print('삭제되었습니다.')
    
    return render(request,'stuWrite.html')