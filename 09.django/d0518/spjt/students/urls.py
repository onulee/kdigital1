from django.urls import include,path
from . import views

app_name='students'  # 페이지내에서 이동할때
urlpatterns = [
    # 학생등록
    path('stuWrite/',views.stuWrite,name='stuWrite'), 
    # 학생등록저장
    path('stuWriteOk/',views.stuWriteOk,name='stuWriteOk'), 
    # 학생전체리스트
    path('stuList/',views.stuList,name='stuList'),
    # 학생상세
    path('<str:s_no>/stuView/',views.stuView,name='stuView'),
    # 학생수정
    path('<str:s_no>stuUpdate/',views.stuUpdate,name='stuUpdate'),
    # 학생수정저장
    path('stuUpdateOk',views.stuUpdateOk,name='stuUpdateOk'),
    # 학생삭제
    path('<str:s_no>/stuDelete/',views.stuDelete,name='stuDelete')
]
