from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from fboard.models import Fboard,Comment
from member.models import Member
from django.db.models import F,Q 
from django.core.paginator import Paginator
from django.core import serializers

# 댓글 수정 저장 update
def commUpdateOk(request):
    c_no = request.GET.get('c_no')
    c_content = request.GET.get('c_content')
    id = request.session.get('session_id')
    print("commUpdateOk : ",c_no,c_content,id)
    # 해당데이터 검색
    qs = Comment.objects.get(c_no=c_no)
    qs.c_content = c_content
    qs.c_date=datetime.now()
    qs.save()
    # ajax으로 전송
    context={'c_no':c_no,'c_content':c_content,'c_date':qs.c_date,'result':'댓글이 수정되었습니다.'}
    return JsonResponse(context)


# 댓글 delete
def commDelete(request):
    c_no = request.GET.get('c_no')
    qs = Comment.objects.get(c_no=c_no)
    qs.delete()
    context={'result':'댓글이 삭제되었습니다.'}
    return JsonResponse(context)


# 댓글 write - Query : dic타입
def commWrite(request):
    # html페이지에서 데이터 가져오기
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    f_no = request.GET.get('f_no')
    fboard = Fboard.objects.get(f_no=f_no)
    pw = request.GET.get('pw')
    content = request.GET.get('content')
    # db에 저장
    qs = Comment(member=member,fboard=fboard,c_pw=pw,c_content=content)
    qs.save()
    # 댓글번호 넘겨줌
    c_no = qs.c_no
    c_date = qs.c_date
    # 저장데이터 : c_no,member,fboard,c_pw,c_content,c_date
    context={"c_no":c_no,"f_no":f_no,"c_pw":pw,"c_content":content,"c_date":c_date}
    return JsonResponse(context)


# 댓글 list - QuerySet : List타입
def commList(request):
    f_no = request.GET.get('f_no')
    print("f_no commList : ",f_no)
    # f_no 하단댓글을 검색
    qs = Comment.objects.filter(fboard=f_no).order_by('-c_no')
    # list타입으로 전송 : safe=False
    clist = list(qs.values()) # [0:q1,1:q2,2:q3]
    return JsonResponse(clist,safe=False) 

    # HttpResponse : json타입 - dic타입
    # clist = serializers.serialize('json',qs)
    # return HttpResponse(clist,content_type='text/json-comment-filtered')
    
    # JsonResponse : dic타입으로 전송
    # context={"clist":clist}
    # # context={'reload_all':False,"clist":clist}
    # return JsonResponse(context) 

# 이벤트
def event(request):
    return render(request,'event.html')

# 이벤트 뷰
def event_view(request):
    print("f_no : ",request.GET.get('f_no'))
    # GET으로 받은 f_no를 넘겨줌.
    context={'f_no':request.GET.get('f_no')}
    return render(request,'event_view.html',context)


# 게시판 수정 함수
def fUpdate(request,nowpage,category,searchword,f_no):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no)
        context = {'board':qs,'nowpage':nowpage,'category':category,'searchword':searchword}
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
        return redirect('fboard:fList',nowpage,category,searchword)

# 게시판 삭제 함수
def fDelete(request,nowpage,category,searchword,f_no):
    qs = Fboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('fboard:fList',nowpage,category,searchword)

# 게시판 답글쓰기 함수
def fReply(request,nowpage,category,searchword,f_no):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no) 
        context={'board':qs,'nowpage':nowpage,'category':category,'searchword':searchword}
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
        
        return redirect('fboard:fList',nowpage,category,searchword)
    

# 게시판 읽기 함수
def fView(request,nowpage,category,searchword,f_no):
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
    context={'board':qs,'boardPrev':qsPrev,'boardNext':qsNext,'nowpage':nowpage,'category':category,'searchword':searchword}
    return render(request,'fView.html',context)

# 게시판 글쓰기 함수
def fWrite(request,nowpage,category,searchword):
    if request.method == 'GET':
        context={"nowpage":nowpage,'category':category,'searchword':searchword}
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
        return redirect('fboard:fList',nowpage,category,searchword)
        
        

# 게시판 리스트 함수
def fList(request,nowpage,category,searchword):
    # GET,POST 포함
    # all,title,content
    if request.method =='POST':
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        print("POST category : ",category,searchword)
    
    print("main category : ",category,searchword)
    # category분류
    if category == 'first':  # GET으로 들어옴.
        qs = Fboard.objects.order_by('-f_group','f_step')
    elif category == 'title':
        qs = Fboard.objects.filter(f_title__contains=searchword)
    elif category == 'content':
        qs = Fboard.objects.filter(f_content__contains=searchword)
    else: # all
        # or 검색 : title or content
        qs = Fboard.objects.filter(Q(f_title__contains=searchword)|Q(f_content__contains=searchword))
        # and 검색 : title and content
        # qs = Fboard.objects.filter(f_title__contains=searchword,f_content__contains=searchword)    
    
    paginator = Paginator(qs,10)     # 1페이지 나타낼수 있는 게시글 수 설정.  
    fList = paginator.get_page(nowpage) # 요청한 페이지의 게시글 10개를 전달
    print("count : ",qs.count)
    context={'fList':fList,'count':qs.count,'nowpage':nowpage,'category':category,'searchword':searchword}
    return render(request,'fList.html',context)
