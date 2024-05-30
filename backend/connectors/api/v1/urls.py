from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135614ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135614", Testconnectors135614ViewSet, basename="testconnectors135614"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
