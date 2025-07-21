from django.urls import path,include
from rest_framework.router import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'categories',CategoryViewSet)
router.register(r'level2categories',Level2CategoryViewsets)
router.register(r'level3categories',Level3CategoryViewsets)

urlpatterns = [
    path('',include(router.urls))
]























# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, Level2CategoryViewSet, Level3CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'level2-categories', Level2CategoryViewSet)
router.register(r'level3-categories', Level3CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
