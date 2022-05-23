from django.urls import include,path
from . import views

app_name='fboard'
urlpatterns = [
    path('fList/',views.fList,name='fList'),
]
