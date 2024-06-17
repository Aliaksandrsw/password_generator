from django.test import TestCase, Client
from django.urls import reverse


class PasswordGeneratorViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('password_gen')

    def test_password_generator_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generator/password_generator.html')

    def test_password_generator_view_post(self):
        form_data = {
            'length': 12,
            'uppercase': True,
            'numbers': True,
            'special': False
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.url)
        self.assertIn('generated_password', self.client.session)


class SendPasswordEmailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('send_password_email')
        session = self.client.session
        session['generated_password'] = 'testpassword'
        session.save()

    def test_send_password_email_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generator/send_password_email.html')
        self.assertEqual(response.context['password'], 'testpassword')

    def test_send_password_email_view_post(self):
        form_data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('password_gen'))
        self.assertNotIn('generated_password', self.client.session)
