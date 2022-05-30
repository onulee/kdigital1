from django.shortcuts import render
# fboard.models 있는 Fboard Model연결
from fboard.models import Fboard

def event(request):
    return render(request,'event.html')

def event_view(request):
    print("f_no : ",request.GET.get('f_no'))
    return render(request,'event_view.html')


def list(request):
    # Fboard모든 데이터 가져옴.
    qs = Fboard.objects.all()
    # qs개수
    count = qs.count
    context = {'fList':qs,'count':count}
    return render(request,'list.html',context)


def fList(request):
    # Fboard모든 데이터 가져옴.
    qs = Fboard.objects.all()
    # qs개수
    count = qs.count
    context = {'fList':qs,'count':count}
    return render(request,'fList.html',context)
    # return render(request,'fList.html',{'fList':qs})
