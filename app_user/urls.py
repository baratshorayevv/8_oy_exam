from django.urls import path
from .views import user_logout, AccountUpdateView, UserRegistration
from django.contrib.auth.views import LoginView



urlpatterns = [
      path('login/', LoginView.as_view(template_name = 'app_user/login.html'), name='login'),
      path('register/', UserRegistration.as_view(), name='register'),
      path('logout/', user_logout, name='logout'),
      path('account/', AccountUpdateView, name='account'),
      # path('update/', update_user, name='update_user'),
]
