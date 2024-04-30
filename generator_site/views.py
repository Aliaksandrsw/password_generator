import sys

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

import password_generator
from .forms import PasswordGeneratorForm
import string
import random


class PasswordGeneratorView(FormView):
    template_name = 'generator/password_generator.html'
    form_class = PasswordGeneratorForm
    success_url = reverse_lazy('password_gen')

    def form_valid(self, form):
        length = int(form.cleaned_data['length'])
        uppercase = form.cleaned_data['uppercase']
        numbers = form.cleaned_data['numbers']
        special = form.cleaned_data['special']

        characters = string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
        if numbers:
            characters += string.digits
        if special:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        messages.success(self.request, f'Сгенерированный пароль: {password}')
        return super().form_valid(form)


class SendPasswordEmailView(FormView):
    template_name = 'generator/send_password_email.html'
    form_class = PasswordGeneratorForm
    success_url = reverse_lazy('password_gen')

    def form_valid(self, form):
        password = self.request.POST.get('password')
        print(password)
        email = form.cleaned_data.get('email')

        if email:
            print(f'Email: {email}')
            print(f'Password in POST data: {password}')
            try:
                send_mail(
                    'Your Generated Password',
                    f'Your generated password is: {password}',
                    'noreply@example.com',
                    [email],
                    fail_silently=False,
                )

                messages.success(self.request, 'Password sent to your email.')
            except Exception as e:
                messages.error(self.request, 'Failed to send password to your email.')

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('password_generator')
