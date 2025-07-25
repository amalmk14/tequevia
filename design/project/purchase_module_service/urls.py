from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import * 
# from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

router = DefaultRouter()

router.register(r'categories',CategoryViewsets)
router.register(r'subcategories',SubCategoryViewsets)
# router.register(r'level3categories',Level3CategoryViewsets)
router.register(r'size',SizeViewsets)
router.register(r'material',MaterialViewsets)
router.register(r'collar',CollarViewsets)
router.register(r'neck',NeckViewsets)
router.register(r'sleeve',SleeveViewsets)
router.register(r'badge',BadgeViewsets)
router.register(r'color',ColorViewsets)
router.register(r'season',SeasonViewsets)
router.register(r'productmaster',ProductMasterViewsets)
router.register(r'productmaster-variant',ProductMasterVariantViewsets)
router.register(r'productmaster-variant-image',ProductMasterVariantImagesViewsets)
router.register(r'platform',PlatformViewsets)
router.register(r'product-platform-mapping',ProductPlatformMappingViewsets)
router.register(r'vendor',VendorViewsets)

urlpatterns = [
    path('',include(router.urls)),
    path('filtered-productmasters/', FilteredProductMasterViewSet.as_view({'get': 'list'})),

    # path('signup/',SignupView.as_view(), name="signup"),
    # path('login/', LoginView.as_view(), name= "login"),
    # path('signout/',SignoutView.as_view(), name="signout"),
    # # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

