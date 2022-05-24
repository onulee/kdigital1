from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('member/',include('member.urls')),
    path('fboard/',include('fboard.urls')),
    path('product/',include('product.urls')),
] 

# 파일 업로드시 url구성
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
