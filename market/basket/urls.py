from rest_framework.routers import DefaultRouter

from basket.views import MyBasketViewSet

router = DefaultRouter()
router.register('', MyBasketViewSet, basename='my_basket')

urlpatterns = router.urls