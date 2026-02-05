from rest_framework.routers import DefaultRouter
from .views import ItemPostViewSet

router = DefaultRouter()
router.register("posts", ItemPostViewSet)

urlpatterns = router.urls