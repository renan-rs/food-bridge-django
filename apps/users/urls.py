from django.contrib.auth import views as auth_views
from django.urls import path
from apps.users.views import SignUpView
from apps.users.forms import CustomAuthenticationForm
app_name = "users"

urlpatterns = [
    path(
        "signup/", 
        SignUpView.as_view(), 
        name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users/login.html",
            authentication_form=CustomAuthenticationForm,
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]