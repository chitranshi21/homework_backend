from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
	user_name = models.CharField(max_length=30)
	age = models.models.IntegerField(nulll=True,blank=True)
	gender = models.CharField(max_length=30,null=True,blank=True)
	is_active = models.BooleanField(null=True,blank=True)
	dt_added = models.DateTimeField(null=True,blank=True)

class UserProfile(models.Model):
	user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
    mobile1 = models.CharField(max_length=30,null=True,blank=True)
    mobile2 = models.CharField(max_length=30,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    user_type = models.CharField(max_length=50,null=True,blank=True)
    dt_added = models.DateTimeField(null=True,blank=True)


class Order(models.Model):
	stage = models.CharField(max_length=200,null=True,blank=True)
	customer = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	issue = models.CharField(max_length=100)
	service_provider = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	dt_created = models.DateTimeField(null=True,blank=True)
	dt_updated = models.DateTimeField(null=True,blank=True)




