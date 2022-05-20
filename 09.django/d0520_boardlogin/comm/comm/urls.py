from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # home연결 - index.html
    path('',include('home.urls')),
    # freeboard app연결
    path('freeboard/',include('freeboard.urls')),
    # member app연결
    path('member/',include('member.urls')),
]
