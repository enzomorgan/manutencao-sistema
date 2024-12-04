from rest_framework.routers import DefaultRouter
from .views import CasaViewSet

router = DefaultRouter()
router.register('casas', CasaViewSet)

urlpatterns = router.urls
