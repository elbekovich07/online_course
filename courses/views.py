from django.shortcuts import render

def index(request):
    return render(request, 'courses/index.html')

def course(request):
    return render(request, 'courses/course.html')

def teacher(request):
    return render(request, 'courses/teacher.html')
