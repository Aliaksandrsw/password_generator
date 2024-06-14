from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import PasswordGeneratorForm
import string
import random
from .tasks import send_password_email


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
        self.request.session['generated_password'] = password
        messages.success(self.request, f'Сгенерированный пароль: {password}')
        return super().form_valid(form)


class SendPasswordEmailView(FormView):
    template_name = 'generator/send_password_email.html'
    form_class = PasswordGeneratorForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields = {'email': form.fields['email']}
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        password = self.request.session.get('generated_password')
        if password:
            context['password'] = password
        return context

    def form_valid(self, form):
        password = self.request.POST.get('password')

        email = form.cleaned_data.get('email')

        if email:
            try:
                send_password_email(password, email)

                messages.success(self.request, 'Пароль отпрвлен на вашу почту')
                del self.request.session['generated_password']
            except Exception as e:
                messages.error(self.request, 'Failed to send password to your email.')

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('password_gen')
