from django.test import TestCase

from app.generator_site.forms import PasswordGeneratorForm


class PasswordGeneratorFormTestCase(TestCase):
    def test_length_choices(self):
        form = PasswordGeneratorForm()
        self.assertEqual(list(form.fields['length'].choices), [(i, str(i)) for i in range(6, 15)])

    def test_length_initial(self):
        form = PasswordGeneratorForm()
        self.assertEqual(form.fields['length'].initial, 8)

    def test_uppercase_initial(self):
        form = PasswordGeneratorForm()
        self.assertTrue(form.fields['uppercase'].initial)

    def test_numbers_initial(self):
        form = PasswordGeneratorForm()
        self.assertTrue(form.fields['numbers'].initial)

    def test_special_initial(self):
        form = PasswordGeneratorForm()
        self.assertTrue(form.fields['special'].initial)

    def test_email_required(self):
        form = PasswordGeneratorForm()
        self.assertFalse(form.fields['email'].required)

    def test_form_valid(self):
        form_data = {
            'length': 10,
            'uppercase': True,
            'numbers': True,
            'special': True,
            'email': 'test@example.com'
        }
        form = PasswordGeneratorForm(data=form_data)
        self.assertTrue(form.is_valid())