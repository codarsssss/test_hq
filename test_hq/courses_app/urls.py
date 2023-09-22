from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, LessonViewSet, ViewViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('lessons', LessonViewSet)
router.register('view', ViewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

