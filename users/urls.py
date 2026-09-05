from .views import SignUpView, LogoutView, PasswordResetView, NewPasswordView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("signup/", SignUpView.as_view()),
    path("signin/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("signout/", LogoutView.as_view()),
    path("password-reset/", PasswordResetView.as_view()),
    path("password-reset-confirm/<uidb64>/<token>/", NewPasswordView.as_view())
]



