from django import forms

from .models import Course, Teacher, Subject


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

