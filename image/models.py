from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.FileField(upload_to="img/%y")
class exp(models.Model):
	name=models.TextField()
	email=models.EmailField()

class login(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	age=models.IntegerField()
	place=models.CharField(max_length=50)
	password=models.CharField(max_length=20)