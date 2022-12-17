from django.db import models
from datetime import datetime

# Create your models here.
class Appuser(models.Model):
    full_name=models.CharField(max_length=200)
    contact=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    usertype=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    class Meta:
        db_table="app_users"

class Course(models.Model):
    title=models.CharField(max_length=100)
    code=models.CharField(max_length=200)

    class Meta:
        db_table="app_courses"
class Student(models.Model):
    first_name=models.CharField(max_length=200)
    middle_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    Blood_Group=models.CharField(max_length=100)
    academic_level=models.CharField(max_length=100)
    academic_status=models.CharField(max_length=100)
    academic_organization=models.CharField(max_length=100)
    academic_score=models.CharField(max_length=100,null=True,blank=True)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    intake= models.CharField(max_length=200,null=True,blank=True)
    shift= models.CharField(max_length=200)
    remarks=models.CharField(max_length=200)
    visited_at=models.DateTimeField(default=datetime.now())

    class Meta:
        db_table="app_students"
