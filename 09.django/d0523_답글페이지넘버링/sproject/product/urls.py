from django.urls import include,path
from . import views

app_name='product'
urlpatterns = [
    path('pWrite/',views.pWrite,name='pWrite'),
    path('pIndex/',views.pIndex,name='pIndex'),
    
]