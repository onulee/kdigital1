from django.shortcuts import render

# 로그인페이지 함수
def login(request):
    return render(request,'login.html')


# 회원전체리스트 함수
def memberList(request):
    return render(request,'memberList.html')
