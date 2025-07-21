from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import * 

router = DefaultRouter()

router.register(r'categories',CategoryViewSet)
router.register(r'level2categories',Level2CategoryViewsets)
router.register(r'level3categories',Level3CategoryViewsets)

urlpatterns = [
    path('',include(router.urls))
]
