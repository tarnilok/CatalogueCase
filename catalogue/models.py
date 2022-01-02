from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
        
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    product_image = models.ImageField(upload_to='productphotos/')
    description = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']
        
class Slider(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True)
    
    @property
    def image(self):
        return self.productId.product_image
    
    def __str__(self):
        return self.productId.name
    
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
        ordering = ['id']
        
class Favourite(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.productId.name
    
    class Meta:
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'
        ordering = ['id']
    
