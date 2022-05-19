from django.shortcuts import redirect, render
from member.models import Member

# 로그인페이지 함수
def login(request):
    if request.method=='GET':
        print('login GET 호출 : login.html ')
        return render(request,'login.html')
    else:
        print('login POST 호출 : loginOk ')
        # session추가
        return redirect('/') 
 
        
    


# 전체회원리스트 함수
def list(request):
    qs = Member.objects.order_by('-m_no')
    context = {'memberList':qs}
    return render(request,'list.html',context)
