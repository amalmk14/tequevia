from rest_framework import serializers
from .models import *
# from django.contrib.auth.password_validation import validate_password
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.db.models import Q

# class SignupSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     class Meta:
#         model = CustomUser
#         fields = ['reference', 'username', 'email', 'phone_number', 'password']

#         def create(self, validate_data):
#             user = CustomUser(
#                 username = validate_data['username'],
#                 email = validate_data['email'],
#                 phone_number = validate_data['phone_number']
#             )
#             user.set_password(validate_data['password'])
#             user.save()
#             return user

# class LoginSerializer(TokenObtainPairSerializer):
#     identifier = serializers.CharField(write_only=True)
#     password = serializers.CharField(write_only=True)

#     def validate(self, attrs):
#         identifier = attrs.get('identifier')
#         password = attrs.get('password')

#         user = CustomUser.object.filter(
#             Q(username=identifier) | Q(email=identifier) | Q(phone_number=identifier)
#             ).first()
        
#         if user is None or not user.check_password(password):
#             raise serializers.ValidationError("Invalid login credentials")
        
#         data = super().validate({
#             'username' : user.username,
#             'password' : password
#         })

#         data['user'] = {
#             'reference' : str(user.reference),
#             'username' : user.username,
#             'email' : user.email,
#             'phone_number' : user.phone_number
#         }

#         return data
    

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
                   
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"
        
class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = "__all__"

class MasterVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterVariant
        fields = "__all__"

class MasterVariantImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterVariantImage
        fields = "__all__"