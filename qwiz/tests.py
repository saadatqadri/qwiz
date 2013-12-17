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
from qwiz.models import Question, Qwiz 

class HomePageTest(TestCase):
	def test_root_url_resolvers_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class QwizAndQuestionModelTest(TestCase):

	def test_saving_and_retrieving_questions(self):

		qwiz = Qwiz()
		qwiz.save()

		first_question = Question()
		first_question.text = 'The first (ever) question'
		first_question.qwiz = qwiz 
		first_question.save()

		second_question = Question()
		second_question.text = 'The second question'
		second_question.qwiz = qwiz
		second_question.save()

		saved_qwizzes = Qwiz.objects.all()
		self.assertEqual(saved_qwizzes.count(), 1)
		self.assertEqual(saved_qwizzes[0], qwiz)

		saved_questions = Question.objects.all()
		self.assertEqual(saved_questions.count(), 2)

		first_saved_question = saved_questions[0]
		second_saved_question = saved_questions[1]

		self.assertEqual(first_saved_question.text, 'The first (ever) question')
		self.assertEqual(first_saved_question.qwiz, qwiz)

		self.assertEqual(second_saved_question.text, 'The second question')
		self.assertEqual(second_saved_question.qwiz, qwiz)

class QwizViewTest(TestCase):

	def test_users_qwiz_template(self):
		qwiz = Qwiz.objects.create()
		response = self.client.get('/qwiz/%d/' % (qwiz.id, ))
		self.assertTemplateUsed(response, 'qwiz.html')

	def test_displays_only_questions_for_that_qwiz(self):
		correct_qwiz = Qwiz.objects.create()
		Question.objects.create(text='Question 1', qwiz=correct_qwiz)
		Question.objects.create(text='Question 2', qwiz=correct_qwiz)

		other_qwiz = Qwiz.objects.create()
		Question.objects.create(text='other Question 1', qwiz=other_qwiz)
		Question.objects.create(text='other Question 2', qwiz=other_qwiz)

		response = self.client.get('/qwiz/%d/' % (correct_qwiz.id,))

		self.assertContains(response, 'Question 1')
		self.assertContains(response, 'Question 2')
		self.assertNotContains(response, 'other Question 1')
		self.assertNotContains(response, 'other Question 2')

	def test_passes_correct_qwiz_to_template(self):
		other_qwiz = Qwiz.objects.create()
		correct_qwiz = Qwiz.objects.create()
		response = self.client.get('/qwiz/%d/' % (correct_qwiz.id, ))
		self.assertEqual(response.context['qwiz'], correct_qwiz)	

class NewQwizTest(TestCase):

	def test_saving_a_POST_request(self):
		self.client.post(
			'/qwiz/new',
			data={'question_text': 'A new question'}
		)
		self.assertEqual(Question.objects.all().count(), 1)
		new_question = Question.objects.all()[0]
		self.assertEqual(new_question.text, 'A new question')

	def test_redirects_after_POST(self):

		response= self.client.post(
			'/qwiz/new',
			data={'question_text': 'A new question'}
		)
		new_qwiz = Qwiz.objects.all()[0]
		self.assertRedirects(response,'/qwiz/%d/' % (new_qwiz.id,))

class NewQuestionTest(TestCase):

	def test_can_save_a_POST_request_to_an_existing_qwiz(self):
		other_qwiz = Qwiz.objects.create()
		correct_qwiz = Qwiz.objects.create()

		self.client.post(
			'/qwiz/%d/new_question' % (correct_qwiz.id, ),
			data = {'question_text': 'A new question for an existing qwiz'}
		)

		self.assertEqual(Question.objects.all().count(), 1)
		new_question = Question.objects.all()[0]
		self.assertEqual(new_question.text, 'A new question for an existing qwiz')
		self.assertEqual(new_question.qwiz, correct_qwiz)

	def test_redirects_to_qwiz_view(self):

		other_qwiz = Qwiz.objects.create()
		correct_qwiz = Qwiz.objects.create()

		response = self.client.post(
			'/qwiz/%d/new_question' % (correct_qwiz.id,),
			data = {'question_text': 'A new question for an existing qwiz'}
		)

		self.assertRedirects(response, '/qwiz/%d/' % (correct_qwiz.id,))
