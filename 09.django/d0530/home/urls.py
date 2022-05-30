from django.urls import path,include
from . import views
app_name=''
urlpatterns = [
    # views.py index함수 호출
    path('',views.index,name='index'),
]