from django.db import models


# from app01 import views
# from .views import *


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=32)
    gender = models.SmallIntegerField()
    age = models.SmallIntegerField()

    class Meta:
        db_table = 'person'

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    gender = models.SmallIntegerField()
    person = models.ManyToManyField(to=Person)

    class Meta:
        db_table = 'teacher'




class Publish(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)

    class Meta:
        db_table = 'publish'


class Book(models.Model):
    name = models.CharField(max_length=32)
    p = models.ForeignKey(to=Publish, to_field='id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'
