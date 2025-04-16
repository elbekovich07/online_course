from django.db import models


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subjects/')
    course_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='courses/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    students = models.PositiveIntegerField(default=0)
    duration = models.DurationField()
    rating = models.FloatField()
    review_count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title



class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teachers/')
    profession = models.CharField(max_length=100)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name