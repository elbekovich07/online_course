import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    course_count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='courses/images/')
    video = models.FileField(upload_to='courses/videos/', null=True, blank=True)
    students_count = models.PositiveIntegerField(default=0)
    duration = models.DurationField(blank=True, null=True)
    rating = models.FloatField(default=0.0)
    reviews_count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



    @property
    def student_count(self):
        return self.students.count()


User = get_user_model()


class Review(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.rating}★)"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name} - {self.course.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.email}")
        super().save(*args, **kwargs)
