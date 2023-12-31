from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    capacity = models.IntegerField(default=30)
    open_seats = models.IntegerField(default=30)