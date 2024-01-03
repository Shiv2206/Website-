from django.db import models

# Create your models here.

class Product(models.Model):
    Product_id=models.AutoField
    Product_name=models.CharField(max_length=20)
    cateogry=models.CharField(max_length=50,default="")
    sub_cateogry=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    Pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    
    
    def __str__(self):
        return self.Product_name
   