from django.urls import path,include
from . import views

app_name='freeboard'
urlpatterns = [
    # fList.html연결
    path('fList/',views.fList,name='fList'),
    # fView.html연결
    path('<str:f_no>/fView',views.fView,name='fView'),
    # fWrite.html연결
    path('fWrite/',views.fWrite,name='fWrite'),
    # fUpdate.html연결
    path('<str:f_no>/fUpdate',views.fUpdate,name='fUpdate'),
    # fDelete연결
    path('<str:f_no>/fDelete',views.fDelete,name='fDelete'),
]
