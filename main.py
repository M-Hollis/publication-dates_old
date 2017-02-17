from file_writer import FileWriter
import parameters
import html


def get_received_date(date_string):
	start = date_string.find("Received ") + 9
	end = date_string.find("Accepted")
		    
	received_date = date_string[start:end]

	return received_date

def get_accepted_date(date_string):
	start = date_string.find("Accepted ") + 9
	end = date_string.find("Published")
		    
	accepted_date = date_string[start:end]

	return accepted_date


writer = FileWriter(parameters.filename)

for volume in reversed(parameters.volume_list):

	for number in range(1,parameters.num_articles+1):

		url = html.build_url(volume, parameters.issue, number)
	    
		try:
			date_string = html.get_date_div(url)
		except:
			print "Some error occurred (URL '",url,"' not available?). Skipping."
			break


		received_date = get_received_date(date_string)
		accepted_date = get_accepted_date(date_string)
	    
		writer.write_to_file(received_date, accepted_date)

writer.close_file()
