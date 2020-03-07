from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>List of Heroes</title>', html)
        self.assertTrue(html.endswith('</html>'))
        self.assertEqual(html, expected_html)

        self.assertTemplateUsed(response,'home.html')
