from rest_framework import routers
router = routers.DefaultRouter()
from .views import SlotViewSet
from django.urls import path

router.register(r"slots", SlotViewSet, basename='slots')

urlpatterns = router.urls
