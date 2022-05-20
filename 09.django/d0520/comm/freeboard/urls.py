from django.urls import path,include
from . import views

app_name='freeboard'
urlpatterns = [
    # fList.html연결
    path('fList/',views.fList,name='fList'),
    # fview.html연결
    path('<str:f_no>/fview',views.fview,name='fview'),
]
