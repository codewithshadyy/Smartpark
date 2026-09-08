
from django.urls import path
from .views import CreateMotorApiView, GetMotorDetails

urlpatterns = [
    path("create", CreateMotorApiView.as_view(), name="create"),
    path("list", GetMotorDetails.as_view())
]
