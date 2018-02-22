# Select journal - must be either "ApJ" or "ApJL"
journal = "ApJ"

# Number of articles to use from each issue
num_articles = 30


# Input parameter validation
def valid(journal, num_articles):
	try:
		if (int(num_articles) < 1):
			return False  # fails if num_articles < 1
	except ValueError:
		return False  # fails if num_articles not an integer

	if journal not in {'APJ', 'APJL', 'apj', 'apjl'}:
		return False

	return True
