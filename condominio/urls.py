from django.contrib import admin
from rest_framework.routers import SimpleRouter
from django.urls import path
from casas.api.views import CasaViewSet
from usuarios.api.views import CorretorViewSet
from usuarios.models import Corretor


router = SimpleRouter()

router.register("casas", CasaViewSet, basename="casas")
router.register("corretorer", CorretorViewSet, basename="corretor")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('corretor/', Corretor.site.urls),
]+router.urls