from django.shortcuts import redirect, render
from member.models import Member

# 로그아웃 함수
def logout(request):
    # session 모두 삭제
    request.session.clear()
    # del request.session['session_id'] # session 1개 삭제시
    return redirect('/')


# 로그인페이지 함수
def login(request):
    if request.method=='GET':
        print('login GET 호출 : login.html ')
        return render(request,'login.html')
    else:
        print('login POST 호출 : loginOk')
        # id, pw
        id = request.POST.get('m_id')
        pw = request.POST.get('m_pw')
        # if not (id and pw):
        #    return render(request,'login.html',{'msg':'id,pw 데이터가 없습니다.'})  
        # 해당되는 id,pw가 없을때 error
        try:
            qs = Member.objects.get(m_id=id,m_pw=pw)
        except Member.DoesNotExist:
            qs = None
        
        # qs확인 없으면 None
        if qs:
            # id,pw확인 로그인가능
            # {} 입력방법 {'memberList':qs,'id':'aaa'}
            request.session['session_id']=qs.m_id
            request.session['session_name'] = qs.m_name
            request.session['msg'] = "정상적으로 로그인이 되었습니다."
            # redirect message 변수전달
            return redirect('/')
        else:
            msg='아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인하세요.'
            return render(request,'login.html',{'message':msg})
                
                
        
        
        
        
        # session추가
        return redirect('/') 
 
        
    


# 전체회원리스트 함수
def list(request):
    qs = Member.objects.order_by('-m_no')
    context = {'memberList':qs}
    return render(request,'list.html',context)
