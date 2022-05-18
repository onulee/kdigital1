from django.urls import include,path
from . import views

app_name='students'  # 페이지내에서 이동할때
urlpatterns = [
    path('stuWrite/',views.stuWrite,name='stuWrite'),
]
