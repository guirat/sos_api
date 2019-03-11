from django.db import models

# Create your models here.
from django.contrib.auth.models import User

EMPTY = {'blank': True, 'null': True}
REQUIRED = {'blank': False, 'null': False}
PRIMARY = {'primary_key': True, 'unique': False}


class Activity(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.CharField(max_length=200, **EMPTY)

    def __str__(self): return self.name


class Member(models.Model):
    SEX = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )

    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE, default=None, **EMPTY)
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.CharField(max_length=200, **REQUIRED)
    cin = models.CharField(max_length=200, **REQUIRED)
    phone_number = models.CharField(max_length=200, **REQUIRED)
    birth_date = models.DateField(max_length=200, **EMPTY)
    sex = models.CharField(max_length=200,choices=SEX, **EMPTY)
    description = models.CharField(max_length=200, **EMPTY)
    activity = models.ManyToManyField(Activity)

    def __str__(self): return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    reference = models.CharField(max_length=255, verbose_name='Reference')
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, **EMPTY)

    def __str__(self): return self.reference
