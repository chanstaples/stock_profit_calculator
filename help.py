import sys
from datetime import datetime
from datetime import date

def exit_program(exitString):
	if(exitString.lower() == "exit"):
		print("Exiting now.")
		sys.exit(1)
	else:
		return False

def get_ticker():
	correct_ticker = False
	while(correct_ticker == False):
		ticker = input("Please enter ticker to be analyzed. Letter case does not matter. To exit, please type 'exit'.\n")
		if(exit_program(ticker) == False):
			if(ticker is None or ticker == ""):
				print("ERROR! Please enter a ticker bub.")
			elif(any(char.isdigit() for char in ticker)):
				print("ERROR! No numbers allowed in ticker.")
			elif(len(ticker) > 5):
				print("ERROR! Enter a valid ticker ya scalywag.")
			else:
				correct_ticker = True
	return ticker.upper()

def get_user_year(ticker):
	correct_year = False
	while(correct_year == False):
		year = input("Please enter the year {} was purchased in format YYYY. To exit, please type 'exit'.\n".format(ticker))
		if(exit_program(year) == False):
			if(len(year) != 4): 
				print("ERROR! Enter in a correct year ya dingus.")
			elif(int(year) < 1792):
				print("ERROR! You have selected a year before the stock market existed.")
			elif(int(year) > date.today().year):
				print("ERROR! You have selected a year in the future.")
			else:
				correct_year=True
	return year

def get_user_month(ticker,year):
	correct_month = False
	while(correct_month == False):
		month = input("Please enter the month {} was purchased in format MM. Current year selected: {}. To exit, please type 'exit'.\n".format(ticker,year))
		if(exit_program(month) == False):
			if(len(month) != 2):
				print("ERROR! Enter in a correct month fool.")
			else:
				month = int(month)
				if(month > 12 or month < 1):
					print("ERROR! Enter in a correct month fool.")
				elif(int(year) == date.today().year and month > date.today().month):
					print("ERROR! Year and month selected is in the future.")
				else:
					correct_month = True
	return month

def get_user_day(ticker,year,month):
	correct_day = False
	while(correct_day == False):
		day = input("Please enter the day {} was purchased in format DD. Current year selected: {} and current month selected: {}. To exit, please type 'exit'.\n".format(ticker,year,month))
		if(exit_program(day) == False):
			if(len(day) != 2):
				print("ERROR! Enter in a correct day bucko.")
			else:
				day = int(day)
				if(day > 31 or day < 0):
					print("ERROR! Enter in a valid day bloke.")
				elif(int(year) == date.today().year and int(month) == date.today().month and day > date.today().day):
					print("ERROR! Year, month, and day selected is in the future.")
				else:
					month = int(month)
					if((month == 4 or month == 6 or month == 9 or month == 11) and day > 30):
						print("ERROR: Incorrect day selected for selected month.")
					elif(month == 2 and int(year) % 4 != 0 and day > 28):
						print("ERROR: Incorrect day selected for selected month.")
					elif(month == 2 and int(year) % 4 == 0 and day > 29):
						print("ERROR: Incorrect day selected for selected month.")
					else:
						correct_day = True
	return day

def get_user_shares(ticker,date):
	correct_shares = False
	while(correct_shares == False):
		shares = input("Please enter number of shares of {} purchased on {}.\n".format(ticker,date))
		shares = int(shares)
		if(shares < 1):
			print("ERROR! Enter a valid amount of shares.")
		else:
			correct_shares = True
	return shares

def getStartDateTime(date):
	datetime1 = datetime.strptime(date,"%m-%d-%Y")
	datetimeEpoch = datetime1.timestamp()
	fixedEpoch = int(datetimeEpoch) - 86400
	return fixedEpoch

def getStartDateTime2(date):
	datetime1 = datetime.strptime(date,"%m-%d-%Y")
	datetimeEpoch = datetime1.timestamp()
	fixedEpoch = int(datetimeEpoch) - 86400 + 34200
	return fixedEpoch

def getProfit(userSharePrice,currentSharePrice):
	profit = currentSharePrice - userSharePrice
	profit = round(profit,2)
	print(profit)
	profitDecimal = str(profit).split(".")[1]
	if(len(profitDecimal) == 1): profit = str(profit) + "0"
	return profit
