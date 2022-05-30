from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # home app urls.py로 연결
    path('',include('home.urls')),
    path('fboard/',include('fboard.urls')),
]
