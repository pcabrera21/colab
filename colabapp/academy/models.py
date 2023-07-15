from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(User):
    bio = models.CharField(max_length=500)


class Student(User):
    pass

class Course(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=500)

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete = models.PROTECT) # = models.CASCADE "elimina todo" // = models.PROTECT "protege la eliminacion"
    teacher = models.ForeignKey(Teacher, on_delete = models.PROTECT)
    start_date = models.DateField()

class Subscription(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.PROTECT)
    student = models.ForeignKey(Student, on_delete = models.PROTECT)