from unittest import TestCase
import parameters as pars


class ParameterTests(TestCase):


	def setUp(self):
		self.test_journal = 'APJ'
		self.test_num_articles = "10"  # input from web app is via a form, so is a string


	def test_input_validation_fails_for_wrong_journal(self):
		value = pars.valid("mnras", self.test_num_articles)

		self.assertFalse(value)


	def test_input_validation_passes_for_uppercase(self):
		value = pars.valid(self.test_journal.upper(), self.test_num_articles)

		self.assertTrue(value)


	def test_input_validation_passes_for_lowercase(self):
		value = pars.valid(self.test_journal.lower(), self.test_num_articles)

		self.assertTrue(value)


	def test_input_validation_fails_for_negative_num_articles(self):
		value = pars.valid(self.test_journal, "-2")

		self.assertFalse(value)


	def test_input_validation_fails_for_zero_num_articles(self):
		value = pars.valid(self.test_journal, "0")

		self.assertFalse(value)


	def test_input_validation_fails_for_non_integer_num_articles(self):
		value = pars.valid(self.test_journal, "2.4")

		self.assertFalse(value)


	def test_input_validation_fails_for_non_number_num_articles(self):
		value = pars.valid(self.test_journal, "dhj")

		self.assertFalse(value)


if __name__ == '__main__':
    main()
