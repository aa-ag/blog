from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import posts.views
import sitepages.views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'), # a best practice is to make this complicated and protected for security reasons
    path('', posts.views.home, name='home'),
    path('posts/<int:post_id>', posts.views.post_details, name='post_details'),
    path('search/', posts.views.search, name='search'),
    path('about/', sitepages.views.about, name='about'),
    path('by/', sitepages.views.by, name='by'),
    path('credentials/', sitepages.views.credentials, name='credentials'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
