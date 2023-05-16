from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=18,null=True,blank=True)
    last_name = models.CharField(max_length=18,null=True,blank=True)
    birth = models.DateField(max_length=10,null=True,blank=True)
    mobile = models.IntegerField(max_length=10,null=True,blank=True)
    gender_types = (
        (1, 'male'),
        (2, 'female'),
        (3, 'other'),
    )
    gender = models.IntegerField(
        choices = gender_types,
    )

class Orders(models.Model):
    order_name = models.CharField(max_length=15,null=True,blank=True)
    order_price = models.IntegerField(max_length=5,null=True,blank=True)
    discount = models.IntegerField(max_length=2,null=True,blank=True)
    quanity_of_order = models.IntegerField(max_length=50,null=True,blank=True)
    order_address = models.TextField(max_length=20,null=True,blank=True)
    order_at = models.DateField(max_length=10,null=True,blank=True)


