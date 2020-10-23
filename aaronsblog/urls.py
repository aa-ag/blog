from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'), # a best practice is to make this complicated and protected for security reasons
    path('', views.home, name='home'),
    path('posts/<int:post_id>', views.post_details, name='post_details'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('by/', views.by, name='by'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
