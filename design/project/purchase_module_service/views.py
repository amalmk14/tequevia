from django.shortcuts import render
from rest_framework import viewsets, filters, generics, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *

# Create your views here.

class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

class LoginView(TokenObtainPairView):
    serializers = LoginSerializer

def SignoutView(APIView):
    permission_class = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error':'refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail':'successfully logedout'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({'error':'invalid or expired token'})

class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_on')
    serializer_class = CategorySerializer

    filter_backend = [filters.SearchFilter]
    search_filter = ['category_name']

class Level2CategoryViewsets(viewsets.ModelViewSet):
    queryset = Level2Category.objects.all().order_by('-created_on')
    serializer_class = Level2Serializer

class Level3CategoryViewsets(viewsets.ModelViewSet):
    queryset = Level3Category.objects.all().order_by('-created_on')
    serializer_class = Level3Serializer

class SizeViewsets(viewsets.ModelViewSet):
    queryset = Size.objects.all().order_by('-created_on')
    serializer_class = Sizeserializer

class MaterialViewsets(viewsets.ModelViewSet):
    queryset = Material.objects.all().order_by('-created_on')
    serializer_class = MasterSerializer

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

class MasterViewsets(viewsets.ModelViewSet):
    queryset = Master.objects.all().order_by('-created_on')
    serializer_class = MasterSerializer

class MasterVariantViewsets(viewsets.ModelViewSet):
    queryset = MasterVariant.objects.all().order_by('-created_on')
    serializer_class = MasterVariantSerializer

class MasterVariantImagesViewsets(viewsets.ModelViewSet):
    queryset = MasterVariantImage.objects.all()
    serializer_class = MasterVariantImagesSerializer                                          
    