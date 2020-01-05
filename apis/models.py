from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length= 200)
    email = models.EmailField(max_length= 100)
    username = models.CharField(max_length= 50)
    phone_no = PhoneNumberField(blank= True)

    def __str__(self):
        return self.username

