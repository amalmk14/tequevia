from django.shortcuts import render
from rest_framework import viewsets, filters, generics, status
from rest_framework.viewsets import ViewSet
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *
from django.db.models import Q


# class SignupView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = SignupSerializer
#     permission_classes = [AllowAny]


# class LoginView(TokenObtainPairView):
#     serializers = LoginSerializer


# class SignoutView(APIView):
#     permission_class = [IsAuthenticated]

#     def post(self, request):
#         refresh_token = request.data.get('refresh')
#         if not refresh_token:
#             return Response({'error':'refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
        
#         try:
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response({'detail':'successfully logedout'}, status=status.HTTP_205_RESET_CONTENT)
#         except Exception:
#             return Response({'error':'invalid or expired token'})


class PlatformViewsets(viewsets.ModelViewSet):
    queryset = Platform.objects.all().order_by('-created_on')
    serializer_class = PlatformSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_on')
    serializer_class = CategorySerializer

    filter_backends = [filters.SearchFilter]
    search_fields= ['category_name']


class SubCategoryViewsets(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all().order_by('-created_on')
    serializer_class = SubCategorySerializer

    filter_backends = [filters.SearchFilter]
    search_fields= ['l2category_name', 'category__category_name']


# class Level3CategoryViewsets(viewsets.ModelViewSet):
#     queryset = Level3Category.objects.all().order_by('-created_on')
#     serializer_class = Level3Serializer

#     filter_backends = [filters.SearchFilter]
#     search_fields= ['l3category_name', 'SubCategory_category__l2category_name', 
#                      'SubCategory_category__category__category_name']


class VendorViewsets(viewsets.ModelViewSet):
    queryset = Vendor.objects.all().order_by('-created_on')
    serializer_class = VendorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['vendor_name', 'city', 'state', 'country']


class SizeViewsets(viewsets.ModelViewSet):
    queryset = Size.objects.all().order_by('-created_on')
    serializer_class = Sizeserializer


class MaterialViewsets(viewsets.ModelViewSet):
    queryset = Material.objects.all().order_by('-created_on')
    serializer_class = MaterialSerializer


class CollarViewsets(viewsets.ModelViewSet):
    queryset = Collar.objects.all().order_by('-created_on')
    serializer_class = CollarSerializer


class NeckViewsets(viewsets.ModelViewSet):
    queryset = Neck.objects.all().order_by('-created_on')
    serializer_class = NeckSerializer


class SleeveViewsets(viewsets.ModelViewSet):
    queryset = Sleeve.objects.all().order_by('-created_on')
    serializer_class = SleeveSerializer


class BadgeViewsets(viewsets.ModelViewSet):
    queryset = Badge.objects.all().order_by('-created_on')
    serializer_class = BadgeSerializer


class ColorViewsets(viewsets.ModelViewSet):
    queryset = Color.objects.all().order_by('-created_on')
    serializer_class = ColorSerializer


class SeasonViewsets(viewsets.ModelViewSet):
    queryset = Season.objects.all().order_by('-created_on')
    serializer_class = SeasonSerializer


class ProductMasterViewsets(viewsets.ModelViewSet):
    queryset = ProductMaster.objects.all().order_by('-created_on')
    serializer_class = ProductMasterSerializer

    filter_backends = [filters.SearchFilter]
    search_fields= ['product_name']


class ProductMasterVariantViewsets(viewsets.ModelViewSet):
    queryset = ProductMasterVariant.objects.all().order_by('-created_on')
    serializer_class = ProductMasterVariantSerializer

    filter_backends = [filters.SearchFilter]
    search_fields= ['product_master_reference__product_name']


class ProductMasterVariantImagesViewsets(viewsets.ModelViewSet):
    queryset = ProductMasterVariantImage.objects.all()
    serializer_class = ProductMasterVariantImagesSerializer

    filter_backends = [filters.SearchFilter]
    search_fields= ['variant_reference__product_master_reference__product_name'] 


class ProductPlatformMappingViewsets(viewsets.ModelViewSet):
    queryset = ProductPlatformMapping.objects.all().order_by('-created_on')
    serializer_class = ProductPlatformMappingSerializer

    filter_backends = [filters.SearchFilter]
    search_fields= ['product_master_reference__product_name', 'platform_reference__name']


## filter normal or category or sub_category
# class FilteredProductMasterViewSet(ViewSet):
#     def list(self, request):
#         category = request.query_params.get('category')
#         sub_category = request.query_params.get('sub_category') 
#         size = request.query_params.get('size')
#         material = request.query_params.get('material')
#         collar = request.query_params.get('collar')
#         neck = request.query_params.get('neck')
#         sleeve = request.query_params.get('sleeve')
#         badge = request.query_params.get('badge')
#         color = request.query_params.get('color')

#         queryset = ProductMaster.objects.all()

#         # Filter by category
#         if category:
#             queryset = queryset.filter(sub_category_reference__category__reference=category)

#         # Filter by sub-category
#         if sub_category:
#             queryset = queryset.filter(sub_category_reference__reference=sub_category)

#         # Filter by variant options
#         if any([size, material, collar, neck, sleeve, badge, color]):
#             variant_filter = Q()

#             if size:
#                 variant_filter &= Q(size_reference__reference=size)
#             if material:
#                 variant_filter &= Q(material_reference__reference=material)
#             if collar:
#                 variant_filter &= Q(collar_reference__reference=collar)
#             if neck:
#                 variant_filter &= Q(neck_reference__reference=neck)
#             if sleeve:
#                 variant_filter &= Q(sleeve_reference__reference=sleeve)
#             if badge:
#                 variant_filter &= Q(badge_reference__reference=badge)
#             if color:
#                 variant_filter &= Q(color_reference__reference=color)

#             variant_productmaster_ids = ProductMasterVariant.objects.filter(
#                 variant_filter,
#                 product_master_reference__in=queryset
#             ).values_list('product_master_reference__reference', flat=True)

#             queryset = queryset.filter(reference__in=variant_productmaster_ids)

#         serializer = ProductMasterNestedSerializer(queryset, many=True)
#         return Response(serializer.data)


from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.db.models import Q

class FilteredProductMasterViewSet(ViewSet):
    def list(self, request):
        category = request.query_params.get('category')
        sub_category = request.query_params.get('sub_category') 
        size = request.query_params.get('size')
        material = request.query_params.get('material')
        collar = request.query_params.get('collar')
        neck = request.query_params.get('neck')
        sleeve = request.query_params.get('sleeve')
        badge = request.query_params.get('badge')
        color = request.query_params.get('color')

        queryset = ProductMaster.objects.all()

        # Filter by category
        if category:
            queryset = queryset.filter(sub_category_reference__category__reference=category)

        # Filter by sub-category
        if sub_category:
            queryset = queryset.filter(sub_category_reference__reference=sub_category)

        # Filter product IDs that have at least one matching variant
        if any([size, material, collar, neck, sleeve, badge, color]):
            variant_filter = Q()
            if size:
                variant_filter &= Q(size_reference__reference=size)
            if material:
                variant_filter &= Q(material_reference__reference=material)
            if collar:
                variant_filter &= Q(collar_reference__reference=collar)
            if neck:
                variant_filter &= Q(neck_reference__reference=neck)
            if sleeve:
                variant_filter &= Q(sleeve_reference__reference=sleeve)
            if badge:
                variant_filter &= Q(badge_reference__reference=badge)
            if color:
                variant_filter &= Q(color_reference__reference=color)

            matching_product_ids = ProductMasterVariant.objects.filter(
                variant_filter,
                product_master_reference__in=queryset
            ).values_list('product_master_reference__reference', flat=True).distinct()

            queryset = queryset.filter(reference__in=matching_product_ids)

        serializer = ProductMasterNestedSerializer(
            queryset, many=True, context={
                'size': size,
                'material': material,
                'collar': collar,
                'neck': neck,
                'sleeve': sleeve,
                'badge': badge,
                'color': color,
            }
        )
        return Response(serializer.data)

