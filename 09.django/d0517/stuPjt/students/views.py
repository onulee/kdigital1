from django.shortcuts import render

def register(request):
    # db접근을 해서 정보를 가져옴.6개
    return render(request,'stu/register.html')