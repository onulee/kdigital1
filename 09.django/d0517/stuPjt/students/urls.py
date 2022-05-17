from django.urls import path,include
from . import views

app_name='students'
urlpatterns = [
    path('stuWrite/',views.stuWrite,name='stuWrite'), # 학생등록
    path('stuList/',views.stuList,name='stuList'),    # 학생전체리스트
    # 간단url : 데이터추가
    path('<str:name>/<str:major>/stuView/',views.stuView,name='stuView'),    # 학생상세
    
    
    # path('stuWriteOk/',views.stuWriteOk,name='stuWriteOk'),
]
