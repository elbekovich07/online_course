from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from django.conf import settings
from .models import Student


@receiver(post_save, sender=Student)
def send_signup_confirmation(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Course Sign Up Confirmation',
            message=f"Hello {instance.name},\n\nYou have successfully signed up for the course: {instance.course.title}.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,

        )