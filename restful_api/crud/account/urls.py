from django.contrib import admin
from django.urls import path
from django.conf import settings
from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView, CreateItem, ReadItem, UpdateItem, DeleteItem
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

    path('items/create/', CreateItem.as_view(), name='create_item'),
    path('items/read/', ReadItem.as_view(), name='read_item'),
    path('items/update/', UpdateItem.as_view(), name='update_item'),
    path('items/delete/', DeleteItem.as_view(), name='delete_item'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)