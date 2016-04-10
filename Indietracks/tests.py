from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from Indietracks.views import homepage
from Indietracks.views import performers

# Create your tests here.
class Homepage(TestCase):

    def testHomepageURL(self):
        found = resolve("/")
        self.assertEqual(found.func, homepage)

    def testHomepageContent(self):
        request = HttpRequest()
        response = homepage(request)
        expectedHTML = render_to_string('home.html', request=request)
        self.assertEqual(response.content.decode(), expectedHTML)


class Performers(TestCase):

    def testPerformerURL(self):
        found = resolve("/performers/")
        self.assertEqual(found.func, performers)

    def testPerformersPageContent(self):
        request = HttpRequest()
        response = performers(request)
        expectedHTML = render_to_string('performers.html', request=request)
        test = response.content.decode()
        self.assertEqual(response.content.decode(), expectedHTML)

    def testAddPerformer(self):
        performerName = "The Four Corners"
        request = HttpRequest()
        request.method = "POST"
        request.POST['performerName'] = performerName
        response = performers(request)
        expectedHTML = render_to_string('performers.html', {'performerName': performerName}, request=request)
        self.assertEqual(response.content.decode(), expectedHTML)





