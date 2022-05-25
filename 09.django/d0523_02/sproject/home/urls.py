from django.urls import include,path
from . import views

# home설정
app_name=''
urlpatterns = [
    path('',views.index,name='index'),
]
