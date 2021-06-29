#help.py
#Created by: Chan Staples
#Date: 06/18/2021

##############################################################################################################################################################################################

#Import Statements

import sys
from datetime import datetime
from datetime import date
import holidays

##############################################################################################################################################################################################

#Order of Methods:
#exit_program
#get_ticker
#get_user_year
#get_user_month
#get_user_day
#get_user_shares
#isHoliday
#getStartDateTime
#fixProfit
#overOneYear
#getProfitAfterTax

##############################################################################################################################################################################################
#This method allows user to exit program by typing exit.
#This method has 1 parameter: the string entered by user.
def exit_program(exitString):
	#This if statement takes the user input, changes it to lower case, and tests if it equal exit.
	if(exitString.lower() == "exit"):
		#If the string equals exit, exit the program.
		print("Exiting now.")
		sys.exit(1)
	#This elif statement checks if the user input is greater than 5 which is not necessary so there is a check for it.
	elif(len(exitString) > 5):
		#If the user input is greater than 5, print an error and return False.
		print("ERROR! Invalid Input!")
		return False
	else:
		#If the string does not equal exit, return False.
		return False

##############################################################################################################################################################################################

#This method retrieves company ticker and ensures ticker is valid.
#This method has no parameters.
def get_ticker():
	correct_ticker = False 
	#This while statement checks if the correct_ticker variable is False, meaning it will keep executing as long as a correct ticker is not entered.
	while(correct_ticker == False):
		ticker = input("Please enter ticker to be analyzed. Letter case does not matter. To exit, please type 'exit'.\n")
		#This if statement checks if the return value of method exit_program is False, meaning the user did not enter exit.
		if(exit_program(ticker) == False):
			#This if statement checks if the ticker is None or empty.
			if(ticker is None or ticker == ""):
				#If the ticker is None or empty, print an error and ask for ticker again.
				print("ERROR! Please enter a ticker bub.")
			#This elif statement checks if there is a digit in the ticker, which is not allowed in company tickers.
			elif(any(char.isdigit() for char in ticker)):
				#If the ticker contains a digit, print an error and ask for ticker again.
				print("ERROR! No numbers allowed in ticker.")
			#This elif statement checks if the length of a ticker is greater than 5, which is not allowed for tickers.
			elif(len(ticker) > 5):
				#If the ticker length is more than 5, print an error and ask for ticker again.
				print("ERROR! Enter a valid ticker ya scalywag.")
			else:
				#If the ticker does not meet any of conditions, return True for correct_ticker variable to end the while loop.
				correct_ticker = True
	return ticker.upper() #Return the ticker in all upper-case. This prevents any issues with case.

##############################################################################################################################################################################################

#This method retrieves year for stock purchase and ensures year entered is valid.
#This method has 1 parameter: user entered ticker.
def get_user_year(ticker):
	correct_year = False
	#This while statement checks if the correct_year variable is False, meaning it will keep executing as long as a correct year is not entered.
	while(correct_year == False):
		year = input("Please enter the year {} was purchased in format YYYY. To exit, please type 'exit'.\n".format(ticker))
		#This if statement checks if the return value of method exit_program is False, meaning the user did not enter exit.
		if(exit_program(year) == False):
			year = int(year) #Convert year to an integer.
			#This if statement checks if the length of the year entered is not equal to 4, which is not a valid year.
			if(len(year) != 4): 
				#If the length of the year entered is not 4, print an error and ask for year again.
				print("ERROR! Enter in a correct year ya dingus.")
			#This elif statement checks if the year entered is less than 1900, which is not a valid year.
			elif(year < 1900):
				#If the year entered is less than 1900, print an error and ask for year again.
				print("ERROR! You have selected a year before the stock market existed.")
			#This elif statement checks if the year is greater than the current date's year which is not allowed because it is the future.
			elif(year > date.today().year):
				#If the year entered is greater than the current year, print an error and ask for year again.
				print("ERROR! You have selected a year in the future.")
			else:
				#If the year entered does not meet any of the conditions, return True for correct_year variable to end the while loop.
				correct_year=True
	return year #Returns year as an integer.

##############################################################################################################################################################################################

#This method retrieves month for stock purchase and ensures month entered is valid.
#This method has 2 parameters: user entered ticker and year.
def get_user_month(ticker,year):
	correct_month = False
	#This while statement checks if the correct_month variable is False, meaning it will keep executing as long as a correct month is not entered.
	while(correct_month == False):
		month = input("Please enter the month {} was purchased in format MM. Current year selected: {}. To exit, please type 'exit'.\n".format(ticker,year))
		#This if statement checks if the return value of method exit_program is False, meaning the user did not enter exit.
		if(exit_program(month) == False):
			#This if statement checks if the length of month entered is not 2, which is an invalid month.
			if(len(month) != 2):
				#If the month entered is not equal to 2, print an error and ask for month again.
				print("ERROR! Enter in a correct month fool.")
			else:
				#If the month entered does have a length of 2, continue to next checks.
				month = int(month) #Convert month to an integer.
				#This if statement checks if the month is greater than 12 or less than 1, which are both invalid months.
				if(month > 12 or month < 1):
					#If the month entered fits either condition, print an error and ask for month again.
					print("ERROR! Enter in a correct month fool.")
				#This elif statement checks if the user entered year equals the current year and user entered month is greater than the current month, which is invalid
				#since this is in the future.
				elif(int(year) == date.today().year and month > date.today().month):
					#If the month entered fit the condition, print an error and ask for month again.
					print("ERROR! Year and month selected is in the future.")
				else:
					#If the month entered does not meet any of the conditions, return True for correct_month variable to end the while loop.
					correct_month = True
	return month #Return month as an integer.

##############################################################################################################################################################################################

#This method retrieves day for stock purchase and ensures day entered is valid. 
#This method has 3 parameters: user entered ticker, year, and month.
def get_user_day(ticker,year,month):
	correct_day = False
	#This while statement checks if the correct_day variable is False, meaning it will keep executing as long as a correct day is not entered.
	while(correct_day == False):
		day = input("Please enter the day {} was purchased in format DD. Current year selected: {} and current month selected: {}. To exit, please type 'exit'.\n".format(ticker,year,month))
		#This if statement checks if the return value of method exit_program is False, meaning the user did not enter exit.
		if(exit_program(day) == False):
			#This if statement checks if the length of day entered is not 2, which is an invalid day.
			if(len(day) != 2):
				#If the day entered has length that is not 2, print an error and ask for day again.
				print("ERROR! Enter in a correct day bucko.")
			else:
				#If day entered has a length of 2, continue to next checks.
				day = int(day) #Convert day to an integer.
				#This if statement checks if day is greater than 31 or less than 0, which is also an invalid day.
				if(day > 31 or day < 0):
					#If the day entered fits either condition, print an error and ask for day again.
					print("ERROR! Enter in a valid day bloke.")
				#This elif statement checks if the year is equal to the current year, the month is equal to the current month, and if the day is greater than the current day
				#which would be an invalid date since it is in the future.
				elif(int(year) == date.today().year and int(month) == date.today().month and day > date.today().day):
					#If the day entered is in the future, print an error and ask for day again.
					print("ERROR! Year, month, and day selected is in the future.")
				else:
					#If day entered passes the conditions, check if day is valid for given month. 
					#Note that the months with 31 days are not checked since there is a check fornot entering a date greater than 31 above. 
					month = int(month) #Convert month to an integer.
					#This if statement checks if the month is April, June, September, or November and if day entered is greater than 30, which is not valid since 
					#these months have only 30 days.
					if((month == 4 or month == 6 or month == 9 or month == 11) and day > 30):
						#If the day entered fits the condition, print an error and ask for day again.
						print("ERROR: Incorrect day selected for selected month.")
					#This elif statement checks if the month is February, that the user entered year is NOT divisible by 4, and the day is greater than 28, which is
					#invalid since non-divisible by 4 years only have 28 days in February.
					elif(month == 2 and int(year) % 4 != 0 and day > 28):
						#If the day entered fits the condition, print an error and ask for day again.
						print("ERROR: Incorrect day selected for selected month.")
					#This elif statement checks if the month is February, that the user entered year is divisible by 4, but the day is greater than 29, which is invalid
					#since years divisible by 4 have only 29 days in February.
					elif(month == 2 and int(year) % 4 == 0 and day > 29):
						#If the day entered fits the condition, print an error and ask for day again.
						print("ERROR: Incorrect day selected for selected month.")
					else:
						#If the day entered does not meet any of the conditions, return True for correct_day variable to end the while loop.
						correct_day = True
	return day #Returns day as an integer.

##############################################################################################################################################################################################

#This method retrieves number of shars for stock purchase and ensures number entered is valid.
#This method has 2 parameters: user ticker and user date. 
def get_user_shares(ticker,date):
	correct_shares = False
	#This while statement checks if the correct_shares variable is False, meaning it will keep executing as long as a valid share number is not entered.
	while(correct_shares == False):
		shares = input("Please enter number of shares of {} purchased on {}.\n".format(ticker,date))
		shares = int(shares) #Changes the shares entered from string to int. 
		#This if statement checks if the number of shares is less than 1, which is not a valid number of shares.
		if(shares < 1):
			#If the number of shares is less than 1, print an error and ask for number of shares again.
			print("ERROR! Enter a valid amount of shares.")
		else:
			#If the number of shares is greater than 1, then return True for correct_shares, which breaks the while loop.
			correct_shares = True
	return shares #Return the number of shares as an integer.

##############################################################################################################################################################################################

#This method determines if date entered is a US Holiday.
#This method has 1 parameter: the date to check if it is a Us Holiday.
def isHoliday(date1):
	us_holidays = holidays.US() #Set new variable us_holidays to holidays.US(), which contains all the dates of US Holidays. 
	holidayTest = us_holidays.get(date1) #Test if date1, which is the user entered date, is a US holiday. 
	#This if statement checks if the holidayTest is None, meaning the date entered by the user is not a holiday.
	if holidayTest is None:
		#If holidayTest is None, return False since the date entered is not a US Holiday.
		return False
	else:
		#If holidayTest is not None, return True since date entered is a US Holiday.
		return True

##############################################################################################################################################################################################

#This method retrieves user's date of stock purchase in Epoch format.
#This method has 1 parameter: the user entered date.
def getStartDateTime(date):
	datetime1 = datetime.strptime(date,"%m-%d-%Y") #Converts the date, which is a string, into a datetime object in format of Month-Day-Year.	
	datetimeEpoch = datetime1.timestamp() #Converts the datetime object into Epoch format.
	#This if statement checks if the datetime object's weekday is 5, meaning it is a Saturday. 
	if(datetime1.weekday() == 5):
		#If the datetime object's weekday is a Saturday, change the datetime object in Epoch format to int and add 34200. This is to match Yahoo Finance's formatting for date.
		#The time is then subtracted by 86400 to change the date to Friday from Saturday since the most recent stock share prices will be for the previous Friday.
		#There are no stock share prices for Saturdays.
		fixedEpoch = int(datetimeEpoch) + 34200 - 86400
	#This elif statement checks if the datetime object's weekday is 6, meaning it is a Sunday.
	elif(datetime1.weekday() == 6):
		#If the datetime object's weekday is a Sunday, change the datetime object in Epoch format to int and add 34200. This is to match Yahoo Finance's formatting for date.
		#The time is then subtracted by 172800 to change the date to Friday from Sunday since the most recent stock share prices will be for the previous Friday.
		#There are no stock share prices for Sundays.
		fixedEpoch = int(datetimeEpoch) + 34200 - 172800
	else:	
		#If the datetime object is not a Saturday or Sunday, change the datetime object in Epoch format to int and only add 34200 to match Yahoo Finance's formatting for date.
		fixedEpoch = int(datetimeEpoch) + 34200
	return fixedEpoch #Return the Epoch of the date as an integer.

##############################################################################################################################################################################################

#This method fixes the profit decimal to always have 2 decimal places.
#This method has 1 parameter: the profit.
def fixProfit(profit):
	profit = round(profit,2) #Rounds profit to 2 decimal places.
	profitDecimal = str(profit).split(".")[1] #Retrieves any integers after the decimal.
	#This if statement checks if the length of the integers after the decimal is 1. If so, a 0 is added to end of the profit to make it a length of 2 integers.
	if(len(profitDecimal) == 1): profit = str(profit) + "0"
	return profit #Returns profit as a string. 

##############################################################################################################################################################################################

#This method determines if user's entered date occurred over 1 year ago. 
#This method has 3 parameters: the user entered year, month, and day.
def overOneYear(year,month,day):
	#This if statement checks if the current year minus the user entered year is less than 1.
	if(date.today().year - int(year) < 1):
		#If the year total is less than 1, return False since if the year entered is 0, then it is the same year and the date did not occur over 1 year ago.
		return False
	#This elif statement checks if the current year minus the user entered year is equal to 1 and the current month minus the user entered month is less than 1.
	elif((date.today().year - int(year) == 1) and (date.today().month - int(month) < 1)):
		#If the month total is less than 1, return False since even though the year is valid, the month entered for the year is within 1 year of the current date.
		return False
	#This elif statement checks if the current year minus the user entered year is equal to 1, the current month minus the user entered month is equal to 0, and the current day minus 
	#the user entered day is less than 1.
	elif((date.today().year - int(year) == 1) and (date.today().month - int(month) == 0) and (date.today().day - int(day) < 1)):
		#If the day total is less than 1, return False even if year and month are valid since day entered is within 1 year of the current date.
		return False
	else:
		#If the date entered doesn't meet any of the other conditions, return True, the user entered date is over 1 year ago.
		return True 

##############################################################################################################################################################################################

#This method determines the net profit and includes estimates for long term and short term capital gains tax rate as well as a loss. 
#This method has 5 parameters: user entered year, month, day, ticker, and number of shares.
def getProfitAfterTax(year,month,day,profit,ticker,shares):
	profit = float(profit) #Convert profit to a float.
	#This if statement checks if profit is over 0.00 and not negative.
	if(profit > 0.00):
		#If profit is over 0.00, use overOneYear method.
		yearBoolean = overOneYear(year,month,day) #Use overOneYear method to determine if the user entered date is over 1 year ago.
		#This if statement checks if yearBoolean is True, meaning the user entered date is over 1 year ago.
		if(yearBoolean == True):
			#If the user entered date is over 1 year ago, print out long term capital gains tax.
			#This section prints out an estimate of the profit afeter long term capital gains tax.
			print("If your {} shares of {} were sold today, you would pay the long term capital gains tax rate on your profit.\n".format(shares,ticker))
			print("If your annual taxable income is less than $40,000, you pay no long term capital gains tax. Your net profit ${} stays the same.".format(profit))
			profit15 = fixProfit(round(profit * 0.85,2)) #Determines profit with 15% tax rate then rounds the total to 2 decimal places and uses fixProfit method.
			print("If your annual taxable income is $40,001 to $441,450 (as of 2021), your long term capital gains tax rate is 15%. Your net profit is ${}.".format(profit15))
			profit20 = fixProfit(round(profit * 0.8,2)) #Determines profit with 20% tax rate then rounds the total to 2 decimal places and uses fixProfit method.
			print("If your annual taxable income is $441,451 or more (as of 2021), your long term capital gains tax rate is 20%. Your net profit is ${}.".format(profit20))
		else:
			#If the user entered date is within 1 year, print out short term capital gains tax. 
			#This section prints out an estimate of the profit after short term capital gains tax.
			print("If your {} shares of {} were sold today, you would pay the short term capital gains tax rate on your profit.".format(shares,ticker))
			print("Short term capital gains tax rate depends on your filing status (Single, Married filing jointly, Married filing separately, head of household) and taxable income.")
			print("In addition to the tax rate, there is also an amount that you will have to pay that depends on your taxable income.")
			print("Due to these variances, the net profits printed below are ONLY the tax rate for 2021. If you would like to explore the tax brackets further, here is a link to learn more: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets.\n")
			profit10 = fixProfit(round(profit*0.9,2)) #Determines profit with 10% tax rate then rounds the total to 2 decimal places and uses fixProfit method.
			print("If your annual tax income is $0-$9,875, then your tax rate is 10%. Your net profit is ${}.".format(profit10))
			profit12 = fixProfit(round(profit*0.88,2)) #Determines profit with 12% tax rate then rounds the total to 2 decimal places and uses fixProfit method.
			print("If your annual tax income is $9,876-$40,125, then your tax rate is 12%. Your net profit is ${}.".format(profit12))
			profit22 = fixProfit(round(profit*0.78,2)) #Determines profit with 22% tax rate then rounds the total to 2 decimal places and uses fixProfit method.
			print("If your annual tax income is $40,126-$85,525, then your tax rate is 22%. Your net profit is ${}.".format(profit22))
			profit24 = fixProfit(round(profit*0.76,2)) #Determines profit with 24% tax rate then rounds the total to 2 decimal places and uses fixProfit method.
			print("If your annual tax income is $85,526-$163,300, then your tax rate is 24%. Your net profit is ${}.".format(profit24))
			profit32 = fixProfit(round(profit*0.68,2)) #Determines profit with 32% tax rate then rounds the total to 2 decimal places and uses fixProfit method.
			print("If your annual tax income is $163,301-$207,350, then your tax rate is 32%. Your net profit is ${}.".format(profit32))
			profit35 = fixProfit(round(profit*0.65,2)) #Determines profit with 35% tax rate then rounds the total to 2 decimal places and uses fixProfit method.
			print("If your annual tax income is $207,351-$518,400, then your tax rate is 35%. Your net profit is ${}.".format(profit35))
			profit37 = fixProfit(round(profit*0.63,2)) #Determines profit with 37% tax rate then rounds the total to 2 decimal places and uses fixProfit method.
			print("If your annual tax income is $518,401 or more, then your tax rate is 37%. Your net profit is ${}.".format(profit37))
	else:
		#If profit is less than 0.00, print capital loss statement.
		print("Your gross profit of {} is negative, meaning that if you sold {} shares of {} now, you can a capital loss on your taxes and can offset stock gains or any other capital gains in the same year.".format(profit,shares,ticker))

##############################################################################################################################################################################################

#EOF

##############################################################################################################################################################################################
