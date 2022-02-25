from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Clients(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations_management")

class Reservation(models.Model):
    date_time = models.DateTimeField()
    number_of_people = models.IntegerField()
    coment = models.TextField(max_length=100)

# Create your models here.
