from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['reference']
    list_display = ['reference', 'category_name']
    fileds = [field.name for field in Category._meta.fields]
    
# admin.site.register(Level2Category)
@admin.register(Level2Category)
class Level2categoryAdmin(admin.ModelAdmin):
    readonly_fields = ['reference']
    list_display = ['reference', 'l2category_name']
    fields = [field.name for field in Level2Category._meta.fields]

# admin.site.register(Level3Category)
@admin.register(Level3Category)
class Level3categoryAdmin(admin.ModelAdmin):
    readonly_fields = ['reference']
    list_display = ['reference', 'l3category_name']
    fields = [field.name for field in Level3Category._meta.fields]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    readonly_fields = ['reference']
    list_display = ['reference', 'size']
    fields = [field.name for field in Size._meta.fields]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    readonly_fields = ['reference']
    list_display = ['reference', 'material']
    fields = [field.name for field in Material._meta.fields]

@admin.register(Collar)
class CollarAdmin(admin.ModelAdmin):
    readonly_fields = ['reference']
    list_display = ['reference', 'collar']
    fields = [field.name for field in Collar._meta.fields]

@admin.register(Neck)
class NeckAdmin(admin.ModelAdmin):
    readonly_fields = ['reference']
    list_display = ['reference', 'neck']
    fields = [field.name for field in Neck._meta.fields]

@admin.register(Sleeve)
class SleeveAdmin(admin.ModelAdmin):
    readonly_fields = ['reference']
    list_display = ['reference', 'sleeve']
    fields = [field.name for field in Sleeve._meta.fields]