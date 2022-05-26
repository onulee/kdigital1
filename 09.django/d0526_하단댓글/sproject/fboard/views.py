from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F 
from django.core.paginator import Paginator

# 게시판 수정 함수
def fUpdate(request,nowpage,f_no):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no)
        context = {'board':qs,'nowpage':nowpage}
        return render(request,'fUpdate.html',context)
    else:
        # 수정form에서 데이터 전달
        id = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('file',None)
        print("file : ",file)
        # db에 수정저장
        qs = Fboard.objects.get(f_no=f_no)
        qs.f_title = title
        qs.f_content = content
        if file:  # file등록이 되었으면 저장함.
            qs.f_file = file
            print("qs.f_file ok")
        
           
        qs.save()
        return redirect('fboard:fList',nowpage)

# 게시판 삭제 함수
def fDelete(request,nowpage,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('fboard:fList',nowpage)

# 게시판 답글쓰기 함수
def fReply(request,nowpage,f_no):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no) 
        context={'board':qs,'nowpage':nowpage}
        return render(request,'fReply.html',context)
    else:
        # id = request.session.session_id
        id = request.POST.get('id')
        print("id:",id)
        member = Member.objects.get(id=id)
        # request 넘어온 데이터타입 : str타입
        group = int(request.POST.get('group'))
        step = int(request.POST.get('step'))
        indent = int(request.POST.get('indent'))
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('file',None)
        # file = request.POST.get('file',None)
        
        # 부모group에서 부모보다 큰 step 1씩증가, gt보다 큰수
        # reboard = Fboard.objects.filter(f_group=group,f_step_gt=step)
        # # F참조객체: db에서 검색을 해서 가져올수 있음.
        # reboard.update(f_step=F('f_step')+1)
        
        # 부모group에서 부모보다 큰 step 1씩증가, gt보다 큰수
        # F참조객체: db에서 검색을 해서 가져올수 있음.
        Fboard.objects.filter(f_group=group,f_step__gt=step).update(f_step=F('f_step')+1)
        
        # step: 출력순서, indent: 들여쓰기
        qs=Fboard(member=member,f_title=title,f_content=content,f_group=group\
            ,f_step=step+1,f_indent=indent+1,f_file=file)
        qs.save() # f_no
        
        return redirect('fboard:fList',nowpage)
    

# 게시판 읽기 함수
def fView(request,nowpage,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    # 게시판리스트- f_group역순정렬, f_step순차정렬
    # qs = Fboard.objects.order_by('-f_group','f_step')
    # 이전글
    try:
        # 답글로 게시글이 등록될때 찾을수 있는 이전글검색
        qs_prev = Fboard.objects.filter(f_group=qs.f_group,f_step__lt=qs.f_step).order_by('-f_group','f_step').last().f_no
    except:  
        # 순차적으로 게시글이 등록될대 찾을수 있는 이전글검색
        try:
            qs_prev = Fboard.objects.filter(f_group__gt=qs.f_group).order_by('-f_group','f_step').last().f_no
        except:
            # 마지막 게시글 선택시 에러 처리
            qs_prev = Fboard.objects.order_by('-f_group','f_step').first().f_no
    
    # 다음글
    try:
        # 답글로 게시글이 등록될때 찾을수 있는 다음글검색
        qs_next = Fboard.objects.filter(f_group=qs.f_group,f_step__gt=qs.f_step).order_by('-f_group','f_step').first().f_no
    except:  
        # 순차적으로 게시글이 등록될대 찾을수 있는 다음글검색
        try:
            qs_next = Fboard.objects.filter(f_group__lt=qs.f_group).order_by('-f_group','f_step').first().f_no
        except:
            # 처음 게시글 선택시 에러 처리
            qs_next = Fboard.objects.order_by('-f_group','f_step').last().f_no
    
            
    print("qs_prev : ",qs_prev)
    qs.f_hit += 1
    qs.save()
    qsPrev = Fboard.objects.get(f_no=qs_prev)
    qsNext = Fboard.objects.get(f_no=qs_next)
    # 이전글 게시글 검색
    context={'board':qs,'boardPrev':qsPrev,'boardNext':qsNext,'nowpage':nowpage}
    return render(request,'fView.html',context)

# 게시판 글쓰기 함수
def fWrite(request,nowpage):
    if request.method == 'GET':
        context={"nowpage":nowpage}
        return render(request,'fWrite.html',context)
    else:
        # form넘어온 데이터
        id = request.POST.get("id")
        member = Member.objects.get(id=id)
        title = request.POST.get("title")
        content = request.POST.get("content")
        file = request.FILES.get('file',None)
        # db 저장
        qs = Fboard(member=member,f_title=title,f_content=content,f_file=file)
        qs.save()
        qs.f_group = qs.f_no
        qs.save()
        return redirect('fboard:fList',nowpage)
        
        

# 게시판 리스트 함수
def fList(request,nowpage):
    qs = Fboard.objects.order_by('-f_group','f_step')
    # 페이징 처리 - request:str타입
    # page = int(request.GET.get('nowpage',1)) # page변수 전달, 없으면 1
    print("nowpage : ",nowpage)
    paginator = Paginator(qs,10)     # 1페이지 나타낼수 있는 게시글 수 설정.  
    fList = paginator.get_page(nowpage) # 요청한 페이지의 게시글 10개를 전달
    context={'fList':fList,'nowpage':nowpage}
    return render(request,'fList.html',context)
