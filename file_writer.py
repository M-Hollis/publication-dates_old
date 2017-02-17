import csv

class FileWriter:

	def __init__(self, filename):
		self.file_handle = open(filename, 'wb')
		self.writer = csv.writer(self.file_handle, lineterminator='\n')

		self.writer.writerow( ('Date received', 'Date accepted') )
		self.writer.writerow( (' ') )

	def write_to_file(self, first_date, second_date):
		self.writer.writerow( (first_date, second_date) )

		print first_date, second_date

	def close_file(self):
		self.file_handle.close()
