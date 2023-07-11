from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    bio = models.CharField(max_length=500)

class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

class Course(models.Model):
    name = models.CharField(max_length=128)
    desription = models.CharField(max_length=500)

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete = models.PROTECT) # = models.CASCADE "elimina todo" // = models.PROTECT "protege la eliminacion"
    teacher = models.ForeignKey(Teacher, on_delete = models.PROTECT)
    start_date = models.DateField()

class Subscription(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.PROTECT)
    student = models.ForeignKey(Student, on_delete = models.PROTECT)