from django.urls import include,path
from . import views

app_name='' # home : index.html
urlpatterns = [
    path('',views.index,name='index')
]
