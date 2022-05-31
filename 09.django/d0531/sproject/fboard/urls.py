from django.urls import include,path
from . import views

app_name='fboard'
urlpatterns = [
    # 리스트,검색
    path('<int:nowpage>/<str:category>/<str:searchword>/fList/',views.fList,name='fList'),
    path('<int:nowpage>/<str:category>/<str:searchword>/fList2/',views.fList2,name='fList2'),
    path('<int:nowpage>/<str:category>/<str:searchword>/fWrite/',views.fWrite,name='fWrite'),
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fView',views.fView,name='fView'),
    # 답글쓰기
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fReply',views.fReply,name='fReply'),
    # 삭제
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fDelete',views.fDelete,name='fDelete'),
    # 수정
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fUpdate',views.fUpdate,name='fUpdate'),
    # 이벤트
    path('event/',views.event,name='event'),
    # 이벤트 view
    path('event_view/',views.event_view,name='event_view'),
    # 댓글 list
    path('commList/',views.commList,name='commList'),
    # 댓글 write
    path('commWrite/',views.commWrite,name='commWrite'),
    # 댓글 delete
    path('commDelete/',views.commDelete,name='commDelete'),
    # 댓글수정저장 updateOk
    path('commUpdateOk/',views.commUpdateOk,name='commUpdateOk'),
    # 차트그리기 chart01
    path('chart01/',views.chart01,name='chart01'),
    # 차트그리기 데이터 가져오기
    path('chart_data/',views.chart_data,name='chart_data'),
    
]
