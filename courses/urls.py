from django.contrib.auth.views import LoginView
from django.urls import path

from .forms import RegisterForm
from .views import IndexView, CourseView, AboutView
from courses import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/', CourseView.as_view(), name='course'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
]
