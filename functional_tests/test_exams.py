from .base import FunctionalTest

class ExamTest(FunctionalTest):

	def test_exam_creation_and_deletion(self):
		self.browser.get("http://localhost:8000")
		self.browser.find_element_by_link_text('Log in').click()
		self.login(True)
		self.browser.find_element_by_partial_link_text('newest').click()
		self.assertEqual(self.browser.current_url, 'http://localhost:8000/courses/14')
		self.browser.find_element_by_link_text('View exams').click()
		self.browser.find_element_by_link_text('Create new exam').click()
		self.assertEqual(self.browser.current_url, 'http://localhost:8000/courses/14/exams/create')
		self.browser.find_element_by_id('id_name').send_keys('Example exam')		
		self.browser.find_element_by_id('id_description').send_keys('Example description')
		self.browser.find_element_by_id('id_date_to_be_taken').send_keys('10/10/2016 10:40')
		self.browser.find_element_by_id('id_submit').click()
		self.assertEqual(self.browser.current_url, 'http://localhost:8000/courses/14/exams/')
		self.browser.find_element_by_partial_link_text('Example exam').click()
		self.browser.find_element_by_id('id_delete').click()
		self.browser.switch_to_alert().accept()
		self.assertEqual(self.browser.current_url, 'http://localhost:8000/courses/14/exams/')
		self.browser.find_element_by_link_text('Log out').click()

	def test_exam_editing(self):
		self.browser.get("http://localhost:8000")
		self.browser.find_element_by_link_text('Log in').click()
		self.login(True)
		self.browser.find_element_by_partial_link_text('newest').click()
		self.browser.find_element_by_link_text('View exams').click()
		self.browser.find_element_by_partial_link_text('newest_exam').click()
		self.browser.find_element_by_id('id_description').clear()
		self.browser.find_element_by_id('id_description').send_keys('Changed')
		self.browser.find_element_by_id('id_submit').click()
		self.assertEqual(self.browser.current_url, 'http://localhost:8000/courses/14/exams/')
		self.browser.find_element_by_link_text('Log out').click()

	def test_exam_questions_editing(self):
		self.browser.get("http://localhost:8000")
		self.browser.find_element_by_link_text('Log in').click()
		self.login(True)
		self.browser.find_element_by_partial_link_text('newest').click()
		self.browser.find_element_by_link_text('View exams').click()
		self.browser.find_element_by_partial_link_text('newest_exam').click()
		self.browser.find_element_by_link_text('Edit questions').click()
		self.browser.find_element_by_id('id_questions_0').click()
		self.browser.find_element_by_id('id_submit').click()
		self.assertEqual(self.browser.current_url, 'http://localhost:8000/courses/14/exams/12')
		self.browser.find_element_by_link_text('Log out').click()

	def test_exam_viewing(self):
		self.browser.get("http://localhost:8000")
		self.browser.find_element_by_link_text('Log in').click()
		self.login(False)
		self.assertEqual(self.browser.current_url, 'http://localhost:8000/courses/s')
		self.browser.find_element_by_partial_link_text('newest').click()
		self.browser.find_element_by_partial_link_text('newest_exam').click()
		self.browser.find_element_by_link_text('Log out').click()