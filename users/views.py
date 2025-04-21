from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from users.forms import LoginForm, RegisterForm


# Create your views here.



def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            password = cd['password']

            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user:
                if user.is_active:
                    login(request, user)

                    send_mail(
                        subject='Login Notification',
                        message=f'Dear {user.username},\n\nYou have successfully logged into your account.',
                        from_email=None,
                        recipient_list=[user.email],
                        fail_silently=True,
                    )

                    return redirect('courses:index')
                else:
                    messages.error(request, 'Disabled account')
            else:
                messages.error(request, 'Email yoki parol noto‘g‘ri!')

    return render(request, 'users/login_register/login_register.html', {'form': form})


def register_page(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            send_mail(
                subject='Welcome to ECourses!',
                message=f"Hello {user.username},\n\nYou have successfully registered on ECourses. We're glad to have you!",
                from_email=None,
                recipient_list=[user.email],
                fail_silently=True,
            )

            return redirect('courses:index')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')

    return render(request, 'users/login_register/login_register.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('courses:index')
