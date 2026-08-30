from .views import SignUpView, LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("signup/", SignUpView.as_view()),
    path("signin/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("signout/", LogoutView.as_view())
]



