from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

# Create your models here.
# from database to frontend page
class Destination(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='static/images')
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    offer=models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name

# saving data from user to database
class Form(models.Model):
    name=models.CharField(max_length=20)
    email_id=models.EmailField(max_length=100)
    gender=models.CharField(max_length=6)
    intrest=models.CharField(max_length=100)
    region=models.CharField(max_length=20)
    feedback=models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name


class Editor(models.Model):
     title=models.CharField(max_length=20)
     
     body=RichTextField(null=True, blank=True)

    #  def_str_(self):
    #     return self.title





# Create your models here.


    