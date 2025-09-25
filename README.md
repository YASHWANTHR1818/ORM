# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<WhatsApp Image 2025-09-13 at 11.18.52_604e6aa4.jpg>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
from django.db import models
from django.contrib import admin

# Create your models here.
```
class car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=50)
    model= models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.DateField()

class carAdmin(admin.ModelAdmin):
    list_display = ('car_id','brand','model','price','year')
```

```from django.contrib import admin
from . models import car, carAdmin
admin.site.register(car, carAdmin)
```


## OUTPUT

![alt text](<Screenshot 2025-09-25 204225.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
