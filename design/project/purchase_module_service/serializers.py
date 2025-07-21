from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Level2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Level2Category
        fields = '__all__'

class level3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Level3Category
        fields = '__all__'