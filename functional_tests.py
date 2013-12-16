#functional_tests.py
from selenium import webdriver
import unittest



class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(1)

	def teardown(self):
		self.browser.quit()

	def test_can_start_a_quiz_and_retrieve_it_later(self):

		#John's heard about a cool new online learning management tool. He goes to check out the homepage
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention class quizzes
		self.assertIn('Quiz', self.browser.title)
		self.fail('Finish the test')

		# He is invited to create a quiz right away. 

		# He types in the first question into a text box: "Have you taken a course on Python before?"

		# When he hits Enter, the page updates, and now the page lists 
		# '1. Have you taken a course on Python before?' as a question in the quiz

		# There is still a text box inviting him to add another quiz question. He enters
		# "Do you know what the term object-oriented programming means?"

		# The page updates again, and shows both questions in the quiz list

		# John wonders whether the site will remember his quiz. Then he sees that the site has generated a unique URL 
		# for his quiz, and there is some explanatory text to that effect

		# John visits that URL - his quiz is still there

		# Satisfied, he moves on to prepare his lecture

if __name__ == '__main__':
	unittest.main()

