from django.urls import path
from django.contrib.auth import views as auth_views

from .views import Register, Logout

urlpatters = [
    path('register/', Register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='/'), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]