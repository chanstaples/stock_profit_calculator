#help.py
#Created by: Chan Staples
#Date: 06/18/2021

##############################################################################################################################################################################################

#Import Statements

import sys
from datetime import datetime
from datetime import date

##############################################################################################################################################################################################

#This method allows user to exit program by typing exit.
def exit_program(exitString):
	if(exitString.lower() == "exit"):
		print("Exiting now.")
		sys.exit(1)
	else:
		return False

##############################################################################################################################################################################################

#This method retrieves company ticker and ensures ticker is valid.
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

##############################################################################################################################################################################################

#This method retrieves year for stock purchase and ensures year entered is valid.
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

##############################################################################################################################################################################################

#This method retrieves month for stock purchase and ensures month entered is valid.
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

##############################################################################################################################################################################################

#This method retrieves day for stock purchase and ensures day entered is valid. 
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

##############################################################################################################################################################################################

#This method retrieves number of shars for stock purchase and ensures number entered is valid.
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

##############################################################################################################################################################################################

#This method retrieves user's date of stock purchase in Epoch format.
def getStartDateTime(date):
	datetime1 = datetime.strptime(date,"%m-%d-%Y")		
	datetimeEpoch = datetime1.timestamp()
	if(datetime1.weekday() == 5):
		fixedEpoch = int(datetimeEpoch) + 34200 + 172800
	elif(datetime1.weekday() == 6):
		fixedEpoch = int(datetimeEpoch) + 34200 + 86400
	else:	
		fixedEpoch = int(datetimeEpoch) + 34200
	return fixedEpoch

##############################################################################################################################################################################################

#This method fixes the profit decimal to always have 2 decimal places.
def fixProfit(profit):
	profit = round(profit,2)
	profitDecimal = str(profit).split(".")[1]
	if(len(profitDecimal) == 1): profit = str(profit) + "0"
	return profit

##############################################################################################################################################################################################

#This method determines if user's date occurred over 1 year ago. 
def overOneYear(year,month,day):
	if(date.today().year - int(year) < 1):
		return False
	elif((date.today().year - int(year) == 1) and (date.today().month - int(month) < 1)):
		return False
	elif((date.today().year - int(year) == 1) and (date.today().month - int(month) == 0) and (date.today().day - int(day) < 1)):
		return False
	else:
		return True 

##############################################################################################################################################################################################

#This method determines the net profit and includes estimates for long term and short term capital gains tax rate as well as a loss. 
def getProfitAfterTax(year,month,day,profit,ticker,shares):
	profit = float(profit)
	if(profit > 0.00):
		yearBoolean = overOneYear(year,month,day)
		if(yearBoolean == True):
			print("If your {} shares of {} were sold today, you would pay the long term capital gains tax rate on your profit.\n".format(shares,ticker))
			print("If your annual taxable income is less than $40,000, you pay no long term capital gains tax. Your net profit ${} stays the same.".format(profit))
			profit15 = fixProfit(round(profit * 0.85,2))
			print("If your annual taxable income is $40,001 to $441,450 (as of 2021), your long term capital gains tax rate is 15%. Your net profit is ${}.".format(profit15))
			profit20 = fixProfit(round(profit * 0.8,2))
			print("If your annual taxable income is $441,451 or more (as of 2021), your long term capital gains tax rate is 20%. Your net profit is ${}.".format(profit20))
		else:
			print("If your {} shares of {} were sold today, you would pay the short term capital gains tax rate on your profit.".format(shares,ticker))
			print("Short term capital gains tax rate depends on your filing status (Single, Married filing jointly, Married filing separately, head of household) and taxable income.")
			print("In addition to the tax rate, there is also an amount that you will have to pay that depends on your taxable income.")
			print("Due to these variances, the net profits printed below are ONLY the tax rate for 2021. If you would like to explore the tax brackets further, here is a link to learn more: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets.\n")
			profit10 = fixProfit(round(profit*0.9,2))
			print("If your annual tax income is $0-$9,875, then your tax rate is 10%. Your net profit is ${}.".format(profit10))
			profit12 = fixProfit(round(profit*0.88,2))
			print("If your annual tax income is $9,876-$40,125, then your tax rate is 12%. Your net profit is ${}.".format(profit12))
			profit22 = fixProfit(round(profit*0.78,2))
			print("If your annual tax income is $40,126-$85,525, then your tax rate is 22%. Your net profit is ${}.".format(profit22))
			profit24 = fixProfit(round(profit*0.76,2))
			print("If your annual tax income is $85,526-$163,300, then your tax rate is 24%. Your net profit is ${}.".format(profit24))
			profit32 = fixProfit(round(profit*0.68,2))
			print("If your annual tax income is $163,301-$207,350, then your tax rate is 32%. Your net profit is ${}.".format(profit32))
			profit35 = fixProfit(round(profit*0.65,2))
			print("If your annual tax income is $207,351-$518,400, then your tax rate is 35%. Your net profit is ${}.".format(profit35))
			profit37 = fixProfit(round(profit*0.63,2))
			print("If your annual tax income is $518,401 or more, then your tax rate is 37%. Your net profit is ${}.".format(profit37))
	else:
		print("Your gross profit of {} is negative, meaning that if you sold {} shares of {} now, you can a capital loss on your taxes and can offset stock gains or any other capital gains in the same year.".format(profit,shares,ticker))

##############################################################################################################################################################################################

#EOF

##############################################################################################################################################################################################
		
