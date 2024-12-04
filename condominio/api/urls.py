from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CondominioViewSet

router = DefaultRouter()
router.register(r'condominios', CondominioViewSet, basename='condominio')

urlpatterns = [
    path('', include(router.urls)),
]
