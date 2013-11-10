#!/usr/bin/env python
#encoding: utf-8
from suds.client import Client
import datetime
import sys, getopt
sys.path.append("lib")
import Gmail

def main(argv):
	"""Empty user & password. We get them from the script parameters"""
	user = ""
	password = ""
	try:
		opts, args = getopt.getopt(argv,"hu:p:",["user=","password="])
	except getopt.GetoptError:
		print 'usage: Euromillions.py -u <GmailAccount> -p <GmailPassword>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h': # Help option (obviously)
			print 'Euromillions.py -u <GmailAccount> -p <GmailPassword>'
			sys.exit()
		elif opt in ("-u", "--user"): # Complete Gmail account i.e.: foo@gmail.com
			user = arg
		elif opt in ("-p", "--password"): # Gmail password
			password = arg
	now = datetime.datetime.now() # Date to ask for the draw
	game_date = now.strftime("%Y-%m-%d") # Date format as we send it to the WS
	date_format_to_show = now.strftime("%d/%m/%Y") # Date format as we show it in the mail
	url = 'http://resultsservice.lottery.ie/ResultsService.asmx?WSDL'
	client = Client(url)
	result = client.service.GetResultsForDate(drawType="EuroMillions", drawDate=game_date) # There are several draw types, we will need EuroMillions
	
	"""Here we set our numbers and the number of players to share the prize with"""
	my_numbers = [1,2,3,4,5]
	my_stars = [1,2]
	players = 1000

	"""Email settings"""
	gmail_user = user
	gmail_pwd = password
	FROM = user
	TO = ['foo1@gmail.com','foo2@gmail.com','foo3@gmail.com'] # It must be a list
	SUBJECT = "Euromillions results"
	TEXT = ""

	try:
		if result != "" and len(result[0]) != 0: # If there would not be any draw, the WS result will be empty, so we ignore that day
			numbers_successes = 0
			stars_successes = 0
			game_numbers = []
			game_stars = []
			prize_amount = 0
			for number in result[0][0].Numbers:
				for n in number[1]:
					if n.Type == "Standard": # It means regular number, not a star
						game_numbers.append(n.Number)
					else: # A star (obviously again)
						game_stars.append(n.Number)
			TEXT += "<h3>Results for Euromillions draw on " + date_format_to_show + "</h3>" # Mail header with the date
			TEXT += "<p>My numbers: <b>" + str(my_numbers) + "</b><br/>Stars: <b>" + str(my_stars) + "</b></p>" # Showing my numbers
			TEXT += "<p>Draw numbers: " + str(game_numbers) + "<br/>Stars: " + str(game_stars) + "</p>" # Showing draw numbers
			for it in my_numbers: # Checking for matches
				if it in game_numbers:
					numbers_successes += 1
			for it in my_stars:
				if it in game_stars:
					stars_successes += 1
			TEXT += "<p>" + str(numbers_successes) + " number/s and " + str(stars_successes) + " successful star/s.<br/>" # Showing numbers and stars which match the current draw
			if numbers_successes != 0:
				if stars_successes == 0:
					successed_set = str(numbers_successes)
				else:
					successed_set = str(numbers_successes) + "+" + str(stars_successes)
				for prizes in result[0][0].Structure:
					for p in prizes[1]:
						if p.Match == successed_set:
							prize_amount = p.Prize
			TEXT += "Premio al cupón <b>" + str(prize_amount) + "€</b>.<br/>" # Total prize amount won
			TEXT += "Total prize <b>" + str(prize_amount) + "€</b>.<br/>" # Total prize amount won
			TEXT += "<b>Shared with " + str(players) + " players, there will be " + str("{0:.2f}".format(prize_amount/float(players))) + "€ each one</b>.</p>" # Each player amount won
			#The email is going to be sent if the prize amount divided by the number of players is greater than 1€
			if prize_amount/float(players) > 0:
				Gmail.send_email(gmail_user, gmail_pwd, FROM, TO, SUBJECT, TEXT)
	except:
		print "An error has occurred. ", sys.exc_info()[0]
if __name__ == "__main__":
	main(sys.argv[1:])
