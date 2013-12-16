"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from qwiz.views import home_page
from qwiz.models import Question 

class HomePageTest(TestCase):
	def test_root_url_resolvers_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new question'

		response = home_page(request)

		self.assertIn('A new question', response.content.decode())

		expected_html = render_to_string(
			'home.html',
			{'new_item_text': "A new question"}
		)
		self.assertEqual(response.content.decode(), expected_html)

class QuestionModelTest(TestCase):

	def test_saving_and_retrieving_questions(self):

		first_question = Question()
		first_question.text = 'The first (ever) question'
		first_question.save()

		second_question = Question()
		second_question.text = 'The second question'
		second_question.save()

		saved_questions = Question.objects.all()
		self.assertEqual(saved_questions.count(), 2)

		first_saved_question = saved_questions[0]
		second_saved_question = saved_questions[1]

		self.assertEqual(first_saved_question.text, 'The first (ever) question')
		self.assertEqual(second_saved_question.text, 'The second question')
		


