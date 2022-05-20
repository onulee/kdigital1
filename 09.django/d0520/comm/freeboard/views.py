from django.http import HttpResponse
from django.shortcuts import render
from freeboard.models import Freeboard

# freeboard List페이지 함수
def fList(request):
    qs = Freeboard.objects.order_by('-f_no') # f_no로 역순정렬
    context = {'fList':qs}
    return render(request,'fList.html',context)
    # return HttpResponse('test')
