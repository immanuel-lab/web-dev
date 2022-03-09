from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Employee(models.Model):
     name=models.CharField(max_length=20)
     emp_id=models.IntegerField(max_length=10)
     phone_num=models.IntegerField(max_length=10)
     salary=models.IntegerField(max_length=10)


class News1(models.Model):
    date = models.DateTimeField()
    image=models.ImageField(upload_to='static/images')
    news=models.CharField(max_length=10000)
     
# class Editor(models.Model):
#      title=models.CharField(max_length=20)
#      date=models.DateField(auto_now_add=True)
#      body=RichTextField(blank=True,null=True)