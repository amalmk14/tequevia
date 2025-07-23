from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import * 
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

router = DefaultRouter()

router.register(r'categories',CategoryViewsets)
router.register(r'level2categories',Level2CategoryViewsets)
router.register(r'level3categories',Level3CategoryViewsets)
router.register(r'size/',SizeViewsets)
router.register(r'material/',MaterialViewsets)
router.register(r'collar/',CollarViewsets)
router.register(r'neck/',NeckViewsets)
router.register(r'sleeve/',SleeveViewsets)
router.register(r'badge/',BadgeViewsets)
router.register(r'color/',ColorViewsets)
router.register(r'master/',MasterViewsets)
router.register(r'master-variant/',MasterVariantViewsets)
router.register(r'master-variant-image/',MasterVariantImagesViewsets)

urlpatterns = [
    path('',include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

