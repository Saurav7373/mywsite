import os
from random import random

from django.db import models


# Create your models here.
#
class Client( models.Model ):
    c_id = models.AutoField( primary_key=True )
    name = models.CharField( max_length=30 )
    email = models.EmailField( max_length=70, default="" )
    phone = models.CharField( max_length=14, default="" )
    dob = models.DateTimeField()
    district = models.CharField( max_length=50 )
    pro = models.CharField( max_length=50 )
    desc = models.TextField( max_length=50 )
    boolChoice = (
        ("M", "Male"), ("F", "Female")
    )
    gender = models.CharField( max_length=1, choices=boolChoice, default="" )

    def __str__(self):
        return self.name


class Contact( models.Model ):
    email = models.EmailField()
    subject = models.CharField( max_length=196 )
    message = models.TextField()

    def __str__(self):
        return self.email


class Image( models.Model ):
    i_id = models.AutoField( primary_key=True )
    name = models.CharField( max_length=30 )
    email = models.EmailField( max_length=70, default="" )
    phone = models.CharField( max_length=14, default="" )
    picture1 = models.ImageField( upload_to="palmpic" )
    picture2 = models.ImageField( upload_to="palmpic" )
    dou1 = models.DateTimeField()
    desc1 = models.TextField( max_length=50 )

    def __str__(self):
        return self.name
