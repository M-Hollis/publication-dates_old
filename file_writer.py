import csv

class FileWriter:

	def __init__(self, filename):
		self.__file_handle = open(filename, 'wb')
		self.__writer = csv.writer(self.__file_handle, lineterminator='\n')

		self.__writer.writerow( ('Date received', 'Date accepted', 'Processing time (days)') )
		self.__writer.writerow( (' ') )


	def write_to_file(self, article):
		dates = article.get_dates()

		self.__writer.writerow(dates)
		print dates[0], dates[1]


	def close_file(self):
		self.__file_handle.close()
