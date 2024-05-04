from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_password_email(password, email):
    subject = f'Ваш сгенерированный пароль: {password}'
    message = f'Ваш сгенерированный пароль: {password}'
    from_email = 'example@ya.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
