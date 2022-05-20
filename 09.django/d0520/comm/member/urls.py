from django.urls import include,path
from . import views

app_name='member'
urlpatterns = [
    # login페이지 연결
    path('login/',views.login,name='login'),
]
