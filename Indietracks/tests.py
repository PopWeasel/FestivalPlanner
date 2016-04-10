from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from Indietracks.views import homepage

# Create your tests here.
class Homepage(TestCase):

    def testHomepageURL(self):
        found = resolve("/")
        self.assertEqual(found.func, homepage)

    def testHomepageContent(self):
        request = HttpRequest()
        response = homepage(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'Festival Planner', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

