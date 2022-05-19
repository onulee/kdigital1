from django.urls import include,path
from . import views

app_name='member'
urlpatterns = [
    # 회원전체리스트
    path('memberList/',views.memberList,name='memberList'),
    path('login/',views.login,name='login'),
]
