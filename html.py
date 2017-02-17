import requests
from BeautifulSoup import BeautifulSoup

apj_base = "http://iopscience.iop.org/article/10.3847/1538-4357/"
apj_base2 = "http://iopscience.iop.org/article/10.3847/0004-637X/"  # different base URL before vol.833 iss.2 for some reason

apjl_base = "http://iopscience.iop.org/article/10.3847/2041-8213/"


def build_url(volume, issue, number):
	
	vol_issue = str(volume) + "/" + str(issue) + "/"

	if volume > 833:
	    url = apj_base + vol_issue + str(number)
	else:
	    url = apj_base2 + vol_issue + str(number)

	return url


def get_date_div(url):
	    
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	        
	dates = soup.find('div', attrs={'class':'col-no-break wd-jnl-art-dates'}).text
	#dates = soup.find('div', attrs={'class':'article-meta'})

	return dates
