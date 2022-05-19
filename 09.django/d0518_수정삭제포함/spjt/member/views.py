from django.shortcuts import render

# 회원정보리스트2 - list.html
def list(request):
    return render(request,'list.html')


# 회원정보리스트
def memberList(request):
    return render(request,'memberList.html')
