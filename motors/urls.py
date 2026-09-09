
from django.urls import path
from .views import CreateMotorApiView, GetMotorDetails, MotorDetailView

urlpatterns = [
    path("create", CreateMotorApiView.as_view(), name="create"),
    path("list", GetMotorDetails.as_view()),
    path("list/<int:pk>/",MotorDetailView.as_view() )
]
