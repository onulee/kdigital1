from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    # http://127.0.0.1:8000/students/
    path('students/',include('students.urls')),
    path('member/',include('member.urls')),
]
