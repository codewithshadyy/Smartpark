
from django.urls import path
from .views import BookingApiView


urlpatterns = [
    path("book/", BookingApiView.as_view(), name='book')
]
