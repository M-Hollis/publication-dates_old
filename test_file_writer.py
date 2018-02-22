from unittest import TestCase
from file_writer import FileWriter
from article import Article
import os
import csv


class FileWriterTests(TestCase):


	def setUp(self):
		test_string = 'DatesReceived 2016 November 21Accepted 2017 January 8Published2017 February 3'
		self.article = Article(test_string)

		self.test_filename = "test_file.csv"
		self.test_path = self.test_filename + "_dates.csv"


	def tearDown(self):
		os.remove(self.test_path)


	def test_writer_creates_file(self):
		writer = FileWriter(self.test_filename)

		self.assertTrue(os.path.isfile(self.test_path))


	def test_writer_writes_dates_to_file(self):
		writer = FileWriter(self.test_filename)
		expected_dates = self.article.get_dates()

		writer.write_to_file(self.article)

		with open(self.test_path, 'rt') as f:
			reader = csv.reader(f, delimiter=',')
			for row in reader:
				self.assertIn(expected_dates[0], row)
				self.assertIn(expected_dates[1], row)


if __name__ == '__main__':
	main()
