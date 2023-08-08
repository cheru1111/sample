from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class CategoryModel(models.Model):
    Category_Name=models.CharField(max_length=70)

class product(models.Model):
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='image/',null=True) 

class CustomerModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    number=models.IntegerField()

class CartModel(models.Model):
    Customer=models.ForeignKey(CustomerModel,on_delete=models.CASCADE,null=True)
    Product=models.ForeignKey(product,on_delete=models.CASCADE,null=True) 

class SubCategoryModel(models.Model):
    Category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)

    SubCategory_Name=models.CharField(max_length=70) 

class OrderModel(models.Model):
    Category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    Customer=models.ForeignKey(CustomerModel,on_delete=models.CASCADE,null=True)
    Product=models.ForeignKey(product,on_delete=models.CASCADE,null=True)           
