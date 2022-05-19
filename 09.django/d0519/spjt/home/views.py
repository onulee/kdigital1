from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # HttpResponse : data형태로 전달
    # return HttpResponse("<h2>테스트</h2>")
