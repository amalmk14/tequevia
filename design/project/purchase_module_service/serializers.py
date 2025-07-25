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


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class ProductPlatformMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPlatformMapping
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


# class Level3Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Level3Category
#         fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
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


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"

        
class ProductMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaster
        fields = "__all__"


class ProductMasterVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMasterVariant
        fields = "__all__"


class ProductMasterVariantImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMasterVariantImage
        fields = "__all__"

        
# class ProductMasterVariantImageNestedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductMasterVariantImage
#         fields = ['reference', 'image', 'alt_text']


# class ProductMasterVariantNestedSerializer(serializers.ModelSerializer):
#     images = ProductMasterVariantImageNestedSerializer(many=True, read_only=True)

#     class Meta:
#         model = ProductMasterVariant
#         fields = [
#             'reference', 'size_reference', 'sleeve_reference', 'neck_reference',
#             'collar_reference', 'material_reference', 'badge_reference', 'color_reference',
#             'price', 'offer_price', 'offer_percentage', 'stock', 'weight',
#             'main_image', 'description', 'tag', 'is_active', 'created_on', 'images'
#         ]


# class ProductMasterNestedSerializer(serializers.ModelSerializer):
#     variants = ProductMasterVariantNestedSerializer(many=True, read_only=True)

#     class Meta:
#         model = ProductMaster
#         fields = [
#             'reference', 'product_name', 'product_code', 'image',
#             'created_on', 'is_active', 'variants'
#         ]

class ProductMasterVariantImageNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMasterVariantImage
        fields = ['reference', 'image', 'alt_text']


class ProductMasterVariantNestedSerializer(serializers.ModelSerializer):
    images = ProductMasterVariantImageNestedSerializer(many=True, read_only=True)

    class Meta:
        model = ProductMasterVariant
        fields = [
            'reference', 'size_reference', 'sleeve_reference', 'neck_reference',
            'collar_reference', 'material_reference', 'badge_reference', 'color_reference',
            'price', 'offer_price', 'offer_percentage', 'stock', 'weight',
            'main_image', 'description', 'tag', 'is_active', 'created_on', 'images'
        ]

    def to_representation(self, instance):
        context = self.context

        # Variant-level filter logic
        if context.get('size') and str(instance.size_reference.reference) != context.get('size'):
            return None
        if context.get('material') and str(instance.material_reference.reference) != context.get('material'):
            return None
        if context.get('collar') and str(instance.collar_reference.reference) != context.get('collar'):
            return None
        if context.get('neck') and str(instance.neck_reference.reference) != context.get('neck'):
            return None
        if context.get('sleeve') and str(instance.sleeve_reference.reference) != context.get('sleeve'):
            return None
        if context.get('badge') and str(instance.badge_reference.reference) != context.get('badge'):
            return None
        if context.get('color') and str(instance.color_reference.reference) != context.get('color'):
            return None

        return super().to_representation(instance)


class ProductMasterNestedSerializer(serializers.ModelSerializer):
    variants = serializers.SerializerMethodField()

    class Meta:
        model = ProductMaster
        fields = [
            'reference', 'product_name', 'product_code', 'image',
            'created_on', 'is_active', 'variants'
        ]

    def get_variants(self, obj):
        variants = obj.variants.all()
        serializer = ProductMasterVariantNestedSerializer(
            variants, many=True, context=self.context
        )
        return [v for v in serializer.data if v is not None]
