from django.db import models
import uuid


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="category-image/")
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Category_name
    


class Level2Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="level2_categories")
    l2category_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="level2-image/")
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.l2category_name

class Level3Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level2_category = models.ForeignKey(Level2Category, on_delete=models.CASCADE, related_name="level3_categories")
    l3category_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="level3-image/")
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.l3category_name
    
class Size(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size = models.CharField(max_length=10)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.size
    
class material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.material
    
class Collar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    collar = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.collar
    
class Neck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    neck = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.neck
    
class Sleeve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sleeve = models.CharField(max_length=250)
    delete_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sleeve
    
class Master(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=250)
    product_code = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    level2_category = models.ForeignKey(Level2Category, on_delete=models.CASCADE, related_name="products")
    level3_category = models.ForeignKey(Level3Category,on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="master-image/")
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name



    
    
    