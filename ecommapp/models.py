from django.db import models
from django.contrib.auth.models import User

# Create your models here.]

class Categories(models.Model):
    Category_name=models.CharField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Category_name
    
class Products(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    Category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    price=models.PositiveBigIntegerField()
    Image=models.ImageField(upload_to="images",null=True)
    description=models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True,null=True)
    quantity=models.IntegerField(default=1)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")    
    )
    status=models.CharField(max_length=100,choices=options,default="in-cart")

class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True,null=True)
    options=(
        ("order-placed","order-placed"),
        ("dispatched","dispatched"),
        ("in-transit","in-transit"),
        ("deliverd","deliverd"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=100,choices=options,default="order-placed")

class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comments=models.CharField(max_length=200)


