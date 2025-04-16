from django.contrib import admin
from courses.models import Subject, Course, Teacher
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','course_count')
    search_fields = ('name',)



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','subject', 'students', 'duration', 'price')
    search_fields = ('subject',)
    list_filter = ('title',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession')
    search_fields = ('full_name','profession',)