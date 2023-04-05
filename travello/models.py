from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
  

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    sub = models.CharField(max_length=220)
    msg = models.TextField()
    date = models.DateField() 

    def __str__(self):
        return self.name

