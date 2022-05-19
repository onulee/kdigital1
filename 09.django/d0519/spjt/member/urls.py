from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    # 전체회원리스트
    path('list/',views.list,name='list'),
    # 로그인
    path('login/',views.login,name='login'),
    # 로그아웃
    path('logout/',views.logout,name='logout'),
]
