from django.contrib import admin
from .models import *


@admin.register(AuthUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ['reference']
    list_display = ['reference', 'phone_number'] 
    # fields = [field.name for field in AuthUser._meta.fields]
    

# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'category_name']
    fileds = [field.name for field in Category._meta.fields]

    
# admin.site.register(SubCategory)
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'category_name']
    fields = [field.name for field in SubCategory._meta.fields]


# admin.site.register(Level3Category)
# @admin.register(Level3Category)
# class Level3categoryAdmin(admin.ModelAdmin):
#     readonly_fields = ['reference']
#     list_display = ['reference', 'l3category_name']
#     fields = [field.name for field in Level3Category._meta.fields]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'size']
    fields = [field.name for field in Size._meta.fields]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'material']
    fields = [field.name for field in Material._meta.fields]


@admin.register(Collar)
class CollarAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'collar']
    fields = [field.name for field in Collar._meta.fields]


@admin.register(Neck)
class NeckAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'neck']
    fields = [field.name for field in Neck._meta.fields]


@admin.register(Sleeve)
class SleeveAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'sleeve']
    fields = [field.name for field in Sleeve._meta.fields]


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'badge']
    fields = [field.name for field in Badge._meta.fields]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'color']
    fields = [field.name for field in Color._meta.fields]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'season']
    fields = [field.name for field in Season._meta.fields]


@admin.register(ProductMaster)
class ProductMasterAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'product_name']


@admin.register(ProductMasterVariant)
class ProductMastervariantAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'get_product_name', 'price', 'stock', 'is_active']

    def get_product_name(self, obj):
        return obj.product_master_reference.product_name
    get_product_name.short_descrition = 'Product_name'


@admin.register(ProductMasterVariantImage)
class ProductMastervariantImageAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'get_variant_name']

    def get_variant_name(self, obj):
        return obj.variant_reference.product_master_reference.product_name
    get_variant_name.short_description = 'Product_name'
    

@admin.register(Vendor)
class vendorAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'vendor_name']


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'name']


@admin.register(ProductPlatformMapping)
class ProductPlatformMappingAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'created_on']
    list_display = ['reference', 'product_master_reference__product_name', 'platform_reference__name']

