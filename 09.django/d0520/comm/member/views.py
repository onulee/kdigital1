from django.shortcuts import redirect, render

# login-get,login-post페이지 함수
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        # login체크 프로그램
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        
        return redirect('/')
