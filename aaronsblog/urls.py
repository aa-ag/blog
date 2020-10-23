from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls), # a best practice is to make this complicated and protected for security reasons
    path('', views.home),
    path('posts/<int:post_id>', views.post_details),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
