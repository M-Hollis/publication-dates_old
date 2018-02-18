from datetime import datetime


class Article:

	def __init__(self, date_string):
		self.date_string = date_string.replace(" ", "")


	def get_dates(self):
		received_date = self.__find_received_date()
		accepted_date = self.__find_accepted_date()

		date_difference = self.__find_difference(received_date, accepted_date)

		dates = [received_date, accepted_date, date_difference]

		return dates


	def get_year(self):
		accepted_date = self.__find_accepted_date()

		return int(accepted_date[0:4])


	def __find_received_date(self):
		start = self.date_string.find("Received") + 8
		end = self.date_string.find("Accepted")

		return self.date_string[start:end]


	def __find_accepted_date(self):
		start = self.date_string.find("Accepted") + 8
		end = self.date_string.find("Published")
		    
		return self.date_string[start:end]


	def __find_difference(self, date1, date2):
		d1 = datetime.strptime(date1, "%Y%B%d")
		d2 = datetime.strptime(date2, "%Y%B%d")
		    
		return abs((d2 - d1).days)
