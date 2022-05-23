from django.urls import include,path
from . import views

app_name='fboard'
urlpatterns = [
    path('fList/',views.fList,name='fList'),
    path('fWrite/',views.fWrite,name='fWrite'),
    path('<str:f_no>/fView',views.fView,name='fView'),
    # 답글쓰기
    path('<str:f_no>/fReply',views.fReply,name='fReply'),
    # 삭제
    path('<str:f_no>/fDelete',views.fDelete,name='fDelete'),
    # 수정
    path('<str:f_no>/fUpdate',views.fUpdate,name='fUpdate'),
]
