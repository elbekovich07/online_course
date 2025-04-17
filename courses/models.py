from django.db import models
from django.utils.text import slugify


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subjects/')
    course_count = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'subjects'


class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='courses/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    students = models.PositiveIntegerField(default=0)
    duration = models.DurationField()
    rating = models.FloatField()
    review_count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'courses'


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teachers/')
    profession = models.CharField(max_length=100)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.full_name