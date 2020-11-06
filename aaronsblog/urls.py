from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import posts.views
import sitepages.views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'), # a best practice is to make this complicated and protected for security reasons
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', posts.views.home, name='home'),
    path('posts/<int:post_id>', posts.views.post_details, name='post_details'),
    path('search/', posts.views.search, name='search'),
    path('about/', sitepages.views.about, name='about'),
    path('by/', sitepages.views.by, name='by'),
    path('credentials/', sitepages.views.credentials, name='credentials'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
