from django.urls import path

from courses import views
from .views import IndexView, CourseView, AboutView

app_name = 'courses'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/', CourseView.as_view(), name='course'),
    path('about/', AboutView.as_view(), name='about'),
]
