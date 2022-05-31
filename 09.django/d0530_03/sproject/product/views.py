from django.shortcuts import redirect, render
from product.models import Product

# 상품 메인함수
def pIndex(request):
    qs = Product.objects.all()
    context = {'pList':qs}
    return render(request,'index2.html',context)

# 상품 등록함수
def pWrite(request):
    if request.method == 'GET':
        return render(request,'pWrite.html')
    else:
        # form넘어온 데이터
        name = request.POST.get("name")
        servings = request.POST.get("servings")
        unitPrice = request.POST.get("unitPrice")
        description = request.POST.get("description")
        category = request.POST.get("category")
        manufacturer = request.POST.get("manufacturer")
        unit = request.POST.get("unit")
        fileName = request.FILES.get('fileName',None)
        # db 저장
        qs = Product(p_name=name,p_servings=servings,p_unitPrice=unitPrice,p_description=description,\
           p_category=category,p_manufacturer=manufacturer,p_unit=unit,p_fileName=fileName)
        qs.save()
        
        return redirect('index')
