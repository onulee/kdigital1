from django.urls import include,path
from . import views

app_name='member'
urlpatterns = [
    path('memberList/',views.memberList,name='memberList'),
    path('list/',views.list,name='list'),
]
