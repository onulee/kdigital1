from django.shortcuts import get_object_or_404, redirect, render
from member.models import Member

# logout페이지 함수
def logout(request):
    request.session.clear()
    return redirect('/')


# login-get,login-post페이지 함수
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        # post로 넘어온 데이터 
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        
        # db에서 id,pw로 검색
        try:
            qs = Member.objects.get(id=id,pw=pw)
            request.session['session_id'] = qs.id
            request.session['session_name'] = qs.name
            request.session['session_nickname'] = qs.nickname
            return redirect('/') 
        except Member.DoesNotExist:
            qs = None
            context={'msg':'아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인 바랍니다.'}
            return render(request,'login.html',context)
        
        # 데이터가 있는지 확인
        # if qs:
        #     request.session['session_id'] = qs.id
        #     request.session['session_name'] = qs.name
        #     request.session['session_nickname'] = qs.nickname
        #     return redirect('/')       
        #     # return render(request,'/index.html',{'msg':'로그인 성공'})       
        # else:
        #     context={'msg':'아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인 바랍니다.'}
        #     return render(request,'login.html',context)
