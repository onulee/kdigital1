from django.shortcuts import render
# fboard.models 있는 Fboard Model연결
from fboard.models import Fboard

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
