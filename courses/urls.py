from django.urls import path
from .views import IndexView, CourseView, TeacherView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/', CourseView.as_view(), name='course'),
    path('teacher/', TeacherView.as_view(), name='teacher'),
    path('about/', AboutView.as_view(), name='about'),
]
