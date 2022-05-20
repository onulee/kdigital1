from django.http import HttpResponse
from django.shortcuts import render
from freeboard.models import Freeboard

# freeboard view페이지 함수
def fview(request,f_no):
    # f_no로 1개 데이터 검색
    qs = Freeboard.objects.get(f_no=f_no)
    context={'fboard':qs}
    return render(request,'fview.html',context)

# freeboard List페이지 함수
def fList(request):
    qs = Freeboard.objects.order_by('-f_no') # f_no로 역순정렬
    context = {'fList':qs}
    return render(request,'fList.html',context)
