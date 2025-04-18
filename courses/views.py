from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from courses.forms import LoginForm, RegisterForm
from courses.models import Course


class IndexView(TemplateView):
    template_name = 'courses/index.html'


class CourseView(TemplateView):
    template_name = 'courses/course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['courses'] = Course.objects.all()

        course_slug = self.kwargs.get('course_slug')
        if course_slug:
            context['course'] = Course.objects.filter(course_slug=course_slug).first()

        return context


class AboutView(TemplateView):
    template_name = 'courses/about.html'


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Successfully logged in.")
                    return redirect('index')
                else:
                    messages.error(request, "Your account has been disabled.")
            else:
                messages.error(request, "Username or password is incorrect.")
    return render(request, 'login_register/login_register.html', {'form': form})


def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    return render(request, 'login_register/login_register.html', {'form': form})


def logout_page(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')
