from django.db import models
from django.contrib import admin

# Create your models here.
class car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=50)
    model= models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.DateField()

class carAdmin(admin.ModelAdmin):
    list_display = ('car_id','brand','model','price','year')

