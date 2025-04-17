from django.urls import path
from .views import IndexView, CourseView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/', CourseView.as_view(), name='course'),
    path('about/', AboutView.as_view(), name='about'),
]
nn