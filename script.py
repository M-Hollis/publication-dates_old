import sys
import html
from article import Article
from file_writer import FileWriter


def run(journal, num_articles):

	# Setup output file, set parameters, and use brief run if testing
	writer = FileWriter(journal)

	num_volumes = 18  # 18 volumes per year
	issue = 1  # sample issue for each volume

	# if len(sys.argv) > 1:
	# 	print "Testing....."
	# 	num_articles = 10
	# 	num_volumes = 1


	# Sample papers accepted in previous year
	date = html.detect_start_volume()
	start_volume = date[0]
	acceptance_year = date[1]

	volumes = range(start_volume-num_volumes+1, start_volume+1)


	# for volume in reversed(volumes):

	# 	# Go to volume/issue contents page, and extract URLs of articles
	# 	articles = html.build_urls(journal, volume, issue)
		
	# 	for num in range(1, num_articles+1):

	# 		# For first 'num_articles' in this volume/issue, try to extract date string from article webpage
	# 		url = articles[num]
		    
	# 		try:
	# 			date_string = html.get_date_div(url)
	# 		except:
	# 			print "Some error occurred (URL '",url,"' not available?). Skipping."
	# 			break

	# 		article = Article(date_string)

	# 		if article.get_year() == acceptance_year:
	# 			writer.write_to_file(article)

	writer.close_file()


if __name__ == "__main__":
    run(parameters.journal, parameters.num_articles)
