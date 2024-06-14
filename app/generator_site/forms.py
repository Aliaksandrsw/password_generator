from django import forms


class PasswordGeneratorForm(forms.Form):
    LENGTH_CHOICES = [(i, str(i)) for i in range(6, 15)]
    length = forms.ChoiceField(choices=LENGTH_CHOICES, initial=8, label="Длина")
    uppercase = forms.BooleanField(initial=True, required=False,label="Заглавные буквы")
    numbers = forms.BooleanField(initial=True, required=False, label="Цифры")
    special = forms.BooleanField(initial=True, required=False, label="Спец символы")
    email = forms.EmailField(required=False, label='Email')
