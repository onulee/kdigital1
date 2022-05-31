from django.shortcuts import render
from product.models import Product

def index(request):
   qs = Product.objects.all()[:6]
   context = {'pList':qs}
   return render(request,'index.html',context)
   # return render(request,'index.html') 
