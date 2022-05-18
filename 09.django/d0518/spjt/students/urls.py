from django.urls import include,path
from . import views

app_name='students'  # 페이지내에서 이동할때
urlpatterns = [
    path('stuWrite/',views.stuWrite,name='stuWrite'), # 학생등록
    path('stuWriteOk/',views.stuWriteOk,name='stuWriteOk'), # 학생등록저장
    # 학생전체리스트
    path('stuList/',views.stuList,name='stuList'),
]
