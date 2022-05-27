from django.shortcuts import render

# index.html연결
def index(request):
    return render(request,'index.html')
