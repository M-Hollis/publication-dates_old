from unittest import TestCase
import html


class HtmlTests(TestCase):


	def setUp(self):
		self.test_vol = 836
		self.test_iss = 2


	def test_can_detect_start_volume_in_current_year(self):
		yearToCover = 2017
		expectedStartVol = 854

		(start_volume, previous_year) = html.detect_start_volume()

		self.assertEqual(yearToCover, previous_year)
		self.assertEqual(expectedStartVol, start_volume)


	def test_html_extracts_correct_div_from_html_page(self):
		expectedDateString = 'DatesReceived2016 November 21Accepted2017 January 8Published2017 February 3'

		dateString = html.get_date_div("http://iopscience.iop.org/article/10.3847/1538-4357/836/1/1")

		self.assertEqual(expectedDateString, dateString)


	def test_html_extracts_article_urls_from_contents_page_apj(self):
		journal = "APJ"
		volume = self.test_vol
		issue = self.test_iss

		expectedArticleUrls = ["http://iopscience.iop.org/article/10.3847/1538-4357/aa5be8","http://iopscience.iop.org/article/10.3847/1538-4357/aa5b8b","http://iopscience.iop.org/article/10.3847/1538-4357/aa5b88","http://iopscience.iop.org/article/10.3847/1538-4357/836/2/152","http://iopscience.iop.org/article/10.3847/1538-4357/836/2/153"]
		#URLs of first 5 articles in this issue

		articleUrls = html.build_urls(journal, volume, issue)
		#URLs of all articles in the issue

		self.assertEqual(expectedArticleUrls, articleUrls[:5])


	def test_html_extracts_article_urls_from_contents_page_apjl(self):
		journal = "APJL"
		volume = self.test_vol
		issue = self.test_iss

		expectedArticleUrls = ["http://iopscience.iop.org/article/10.3847/2041-8213/836/2/L17","http://iopscience.iop.org/article/10.3847/2041-8213/aa5dab","http://iopscience.iop.org/article/10.3847/2041-8213/aa5cb0","http://iopscience.iop.org/article/10.3847/2041-8213/aa5eb0","http://iopscience.iop.org/article/10.3847/2041-8213/aa5dee"]
		#URLs of first 5 articles in this issue

		articleUrls = html.build_urls(journal, volume, issue)
		#URLs of all articles in the issue

		self.assertEqual(expectedArticleUrls, articleUrls[:5])


if __name__ == '__main__':
	main()
