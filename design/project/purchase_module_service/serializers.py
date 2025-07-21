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

class Level3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Level3Category
        fields = '__all__'

class Sizeserializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"

class CollarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collar
        fields = "__all__"

class NeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neck
        fields = "__all__"

class SleeveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleeve
        fields = "__all__"

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = "__all__"
        
                
        
        