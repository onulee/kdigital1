from django.urls import include,path
from . import views

app_name='fboard'
urlpatterns = [
    # 리스트,검색
    path('<int:nowpage>/<str:category>/<str:searchword>/fList/',views.fList,name='fList'),
    path('<int:nowpage>/<str:category>/<str:searchword>/fWrite/',views.fWrite,name='fWrite'),
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fView',views.fView,name='fView'),
    # 답글쓰기
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fReply',views.fReply,name='fReply'),
    # 삭제
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fDelete',views.fDelete,name='fDelete'),
    # 수정
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fUpdate',views.fUpdate,name='fUpdate'),
    
]
