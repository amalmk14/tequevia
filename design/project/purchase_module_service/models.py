from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class AuthUser(AbstractUser):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=15, unique=True)
    is_employ = models.BooleanField(blank=True,null=True)
    is_admin = models.BooleanField(blank=True,null=True)
    is_shop = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return self.phone_number


class Platform(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, unique=True)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="category-image/")
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sub_categories")
    category_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="subcategory-image/")
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


# class Level3Category(models.Model):
#     reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     level2_category = models.ForeignKey(Level2Category, on_delete=models.CASCADE, related_name="level3_categories")
#     l3category_name = models.CharField(max_length=250)
#     image = models.ImageField(upload_to="level3-image/")
#     delete_status = models.BooleanField(default=False)
#     created_on = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.l3category_name


class Vendor(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vendor_name


class Size(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size = models.CharField(max_length=10)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.size


class Material(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.material


class Collar(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    collar = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.collar


class Neck(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    neck = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.neck


class Sleeve(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sleeve = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sleeve


class Badge(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    badge = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.badge


class Color(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color = models.CharField(max_length=250)
    color_code = models.CharField(max_length=100)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.color
    

class Season(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    season = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.season


class ProductMaster(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=250)
    product_code = models.CharField(max_length=250)
    sub_category_reference = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="master-image/")
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    platform_reference = models.ManyToManyField(Platform, default="products")

    def __str__(self):
        return self.product_name


class ProductMasterVariant(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    product_master_reference = models.ForeignKey(ProductMaster, on_delete=models.CASCADE, related_name="variants")
    size_reference = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    sleeve_reference = models.ForeignKey(Sleeve, on_delete=models.SET_NULL, null=True)
    neck_reference = models.ForeignKey(Neck, on_delete=models.SET_NULL, null=True)
    collar_reference = models.ForeignKey(Collar, on_delete=models.SET_NULL, null=True)
    material_reference = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    badge_reference = models.ForeignKey(Badge, on_delete=models.SET_NULL, null=True)
    color_reference = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    season_reference = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    offer_percentage = models.IntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    weight = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='variant-main/', null=True, blank=True)
    description = models.TextField(blank=True,null=True)
    tag = models.CharField(max_length=250,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.master_reference.product_name} - {self.size} - {self.material}"


class ProductMasterVariantImage(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    variant_reference = models.ForeignKey(ProductMasterVariant, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="variant-images/")
    alt_text = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.variant}"
    

class ProductPlatformMapping(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_master_reference = models.ForeignKey(ProductMaster, on_delete=models.CASCADE, default='platforms')
    platform_reference = models.ForeignKey(Platform, on_delete=models.CASCADE, default='platforms')
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    