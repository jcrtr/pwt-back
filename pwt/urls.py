from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pwt import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include('category.urls')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('order.urls')),
    path('api/v1/auth/', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
