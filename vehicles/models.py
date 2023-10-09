from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vehicles(models.Model):
    name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    km_driven=models.PositiveIntegerField()
    date=models.DateField(auto_now_add=True)
    owner_type=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    location=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    img=models.ImageField(upload_to="images",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    



