from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, LessonViewSet, ViewViewSet, ProductStatsAPIView

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('lessons', LessonViewSet)
router.register('views', ViewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-stats/', ProductStatsAPIView.as_view(), name='product-stats'),
]