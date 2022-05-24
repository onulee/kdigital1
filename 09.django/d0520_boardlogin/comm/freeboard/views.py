from django.http import HttpResponse
from django.shortcuts import redirect, render
from freeboard.models import Freeboard

# freeboard fDelete 함수
def fDelete(request,f_no):
    qs = Freeboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('/freeboard/fList')

# freeboard fUpdate페이지 함수
def fUpdate(request,f_no):
    if request.method=='GET':
        qs = Freeboard.objects.get(f_no=f_no)
        context = { 'fboard':qs }
        return render(request,'fUpdate.html',context)
    else:
        qs = Freeboard.objects.get(f_no=f_no)
        qs.f_title = request.POST.get('title')
        qs.f_content = request.POST.get('content')
        qs.save()
        return redirect('/freeboard/fList')


# freeboard fWrite페이지 함수
def fWrite(request):
    if request.method=='GET':
        return render(request,'fWrite.html')
    else:
       # f_no,
       # f_group = f_no와 같아야 함.
       # form request데이터 읽기
       id = request.POST.get('id')
       f_title = request.POST.get('title')
       f_content = request.POST.get('content')
       # db에 데이터 저장
       qs = Freeboard(id=id,f_title=f_title,f_content=f_content)
       qs.save()
       # f_no는 AutoField이기 때문에 insert때 생성, f_group에 넣음.
       qs.f_group = qs.f_no
       qs.save()  
       return redirect('freeboard:fList')      
        

# freeboard fView페이지 함수
def fView(request,f_no):
    # f_no로 1개 데이터 검색
    qs = Freeboard.objects.get(f_no=f_no)
    context={'fboard':qs}
    return render(request,'fview.html',context)

# freeboard fList페이지 함수
def fList(request):
    print("session_id : ",request.session.get("session_id"))
    qs = Freeboard.objects.order_by('-f_no') # f_no로 역순정렬
    context = {'fList':qs}
    return render(request,'fList.html',context)
