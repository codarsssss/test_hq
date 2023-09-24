from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, LessonViewSet, ViewViewSet, ProductStatsAPIView

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('lessons', LessonViewSet)
router.register('views', ViewViewSet)

# Создаем новый роутер для корневого представления API
root_router = routers.DefaultRouter()
root_router.registry.extend(router.registry)

# Добавляем 'product-stats' в корневое представление API
root_router.register('product-stats', ProductStatsAPIView, basename='product-stats')

urlpatterns = [
    path('', include(root_router.urls)),
]