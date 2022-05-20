from django.shortcuts import render

# index페이지 연결
def index(request):
    return render(request,'index.html')