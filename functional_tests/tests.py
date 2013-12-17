from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import unittest

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(1)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_qwiz_table(self, row_text):
		table = self.browser.find_element_by_id('id_qwiz_table')
		rows = table.find_elements_by_tag_name('td')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_quiz_and_retrieve_it_later(self):

		#John's heard about a cool new online learning management tool. He goes to check out the homepage
		self.browser.get(self.live_server_url)
		
		# He notices the page title and header mention class quizzes
		self.assertIn('Qwiz', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Qwiz', header_text)

		# He is invited to create a quiz right away. 

		inputbox = self.browser.find_element_by_id('id_new_question')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a quiz question'
		)
		# He types in the first question into a text box: "Have you taken a course on Python before?"

		inputbox.send_keys('Have you taken a course on Python before?')

		# When he hits Enter, the page updates, and now the page lists 
		# '1. Have you taken a course on Python before?' as a question in the quiz

		inputbox.send_keys(Keys.ENTER)
		john_qwiz_url = self.browser.current_url 
		self.assertRegexpMatches(john_qwiz_url, '/qwiz/.+')
		self.check_for_row_in_qwiz_table('1: Have you taken a course on Python before?')

		# There is still a text box inviting him to add another quiz question. He enters
		# "Do you know what the term object-oriented programming means?"

		inputbox = self.browser.find_element_by_id('id_new_question')
		inputbox.send_keys('Do you know what the term object-oriented programming means?')
		inputbox.send_keys(Keys.ENTER)

		# The page updates again, and shows both questions in the quiz list
		
		self.check_for_row_in_qwiz_table('1: Have you taken a course on Python before?')
		self.check_for_row_in_qwiz_table('2: Do you know what the term object-oriented programming means?')

		# A new user, Francis comes along to the site.
		self.browser.quit()
		# We use a new browser session to ensure that no information 
		# of John's is coming through from cookies
		self.browser = webdriver.Firefox()

		# Francis visits the home page. Ther eis no sign of John's quiz.

		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('1: Have you taken a course on Python before?', page_text)
		self.assertNotIn('object-oriented programming means?', page_text)

		# Francis starts a new quiz by enter a new question
		inputbox = self.browser.find_element_by_id('id_new_question')
		inputbox.send_keys('Are you enjoying this class?')
		inputbox.send_keys(Keys.ENTER)

		# Francis get his own unique URL
		francis_qwiz_url = self.browser.current_url
		self.assertRegexpMatches(francis_qwiz_url, '/qwiz/.+')
		self.assertNotEqual(francis_qwiz_url, john_qwiz_url)

		# Again, there is no trace of John's qwiz
		page_text = self.browser.find_element_by_tag_name('body').text 
		self.assertNotIn('Python before', page_text)
		self.assertIn('enjoying this class', page_text)

		# Satisfied, Francis moves on 

		self.fail("Finish the test!")

		# John visits that URL - his quiz is still there
		# Satisfied, he moves on to prepare his lecture
		# Once John has entered the text for the question, he enters the answer type and the possible answers to the question. For the first question
		# The answer is multiple choice, Yes or No. John clicks on the multiple choice answer type and enters the two options.

		# John also specifies the answer to the question
		# John shares the link to the quiz with his students. He wants to make sure that his students have absorbed the material
		# that he delivered during the lecture

		# Katie is a student in John's class, and is reading the lecture when she see's a note from John to answer the Qwiz

		# Katie clicks on the link, and she is presented with the qwiz interface. She reads the first question, and she's taken a course on Python 
		# before, so she decides to answer yes.

		# As Katie clicks on the "Yes" button, John is observing the answers update.

		# Analytics on time spent before answering

	def test_layout_and_styling(self):

		# John goes to the home page
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)

		# He notices the input box is nicely centered
		inputbox = self.browser.find_element_by_tag_name('input')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=3
		)

		# He starts a new list and sees the inputbo is nicely centered there too

		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_tag_name('input')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=3
		)


