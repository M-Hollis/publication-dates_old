from datetime import datetime
import requests
from BeautifulSoup import BeautifulSoup


def detect_start_volume():
	current_year = datetime.now().year
	
	r = requests.get("http://iopscience.iop.org/journal/0004-637X")
	soup = BeautifulSoup(r.content)

	volumes = soup.find('select', attrs={'id':'allVolumesSelector'}).text  # 'Journal archive' dropdown menu

	# Find first volume of input year
	pos = volumes.rfind(str(current_year))  # index of first occurrence of current year in list of volumes
	vol = int(volumes[pos-5:pos-2])  # get just the number out of the string

	# Find first February volume of current year by adding 2
	start_volume = vol + 2
	
	return (start_volume, current_year-1)


def build_urls(journal, volume, issue):

	base_url = "http://iopscience.iop.org"

	contentsPageUrl = __build_contents_page_url(base_url, journal, volume, issue)
	# URL of contents page listing all articles in a given vol. and iss. of the journal

	articleUrls = __get_article_urls(base_url, contentsPageUrl)
	# URLs of all articles extracted from contents page

	return articleUrls


def get_date_div(url):
	    
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	        
	dates = soup.find('div', attrs={'class':'col-no-break wd-jnl-art-dates'}).text
	#dates = soup.find('div', attrs={'class':'article-meta'})

	return dates


def __build_contents_page_url(base_url, journal, volume, issue):

	if journal == "APJ":
		journal_code = "/0004-637X/"
	elif journal == "APJL":
		journal_code = "/2041-8205/"

	contentsPageUrl = base_url + "/issue" + journal_code + str(volume) + "/" + str(issue)

	return contentsPageUrl


def __get_article_urls(base_url, url):

	r = requests.get(url)
	soup = BeautifulSoup(r.content)

	articleUrls = []

	for article in soup.findAll('a', attrs={'class':'art-list-item-title'}):
		url = article.attrs[0][1]
		articleUrls.append(base_url + url.encode('utf-8'))

	return articleUrls
