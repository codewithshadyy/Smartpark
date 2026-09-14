from django.urls import path
from .views import CreateSLotApiView, ListSLotsApiView


urlpatterns = [
    path("create/", CreateSLotApiView.as_view()),
    path("list/", ListSLotsApiView.as_view())
]
