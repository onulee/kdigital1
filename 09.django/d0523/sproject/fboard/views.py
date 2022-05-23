from django.shortcuts import render
from fboard.models import Fboard
from member.models import Member

# 게시판 읽기 함수
def fView(request,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    context={'board':qs}
    return render(request,'fView.html',context)

# 게시판 글쓰기 함수
def fWrite(request):
    if request.method == 'GET':
        return render(request,'fWrite.html')
    else:
        id = request.POST.get("id")
        member = Member.objects.get(id=id)
        title = request.POST.get("title")
        content = request.POST.get("content")
        file = request.POST.get("f_file",None)
        
        qs = Fboard()

# 게시판 리스트 함수
def fList(request):
    qs = Fboard.objects.order_by('-f_group','f_step')
    context={'fList':qs}
    return render(request,'fList.html',context)
