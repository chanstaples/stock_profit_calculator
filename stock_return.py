#stock_return.py
#Created by: Chan Staples
#Date: 06/18/2021

##############################################################################################################################################################################################

#Import Statements

import sys
import requests
import json
from datetime import datetime
from datetime import date
from help import *

##############################################################################################################################################################################################

#Script Execution Section

#This section retrieves user information.
ticker = get_ticker() #Get user ticker.
year = get_user_year(ticker) 
month = get_user_month(ticker,year)
day = get_user_day(ticker,year,month)
date1 = "{}-{}-{}".format(month,day,year) #Combines the day, month, and year into MM-DD-YYYY format.
shares = get_user_shares(ticker,date1)
print("Beginning calculation.\n")

#This section parses and formats the user entered date and current date to prepare for retrieving the share prices.
#This if statement uses the isHoliday method to determine if the user entered date is a holiday.
if(isHoliday(date1) == False):
	#If the date is not a US holiday, get the user's date in Epoch time.
	user_datetime = getStartDateTime(date1)
else:
	#If the date is a US holiday, subtract the day by 1.
	day = int(day) - 1
	date1 = "{}-{}-{}".format(month,day,year) #Combine the day, month, and year again but with the new day.
	user_datetime = getStartDateTime(date1) #Get the user's date in Epoch time.
current_day = datetime.now().timestamp() #Gets the current date's time in Epoch format.
current_day = int(current_day) #Changes the Epoch format to an integer.

#This section prepares program to retrieve information from Yahoo Finance.
URL="https://finance.yahoo.com/quote/{}/history?period1={}&period2={}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true".format(ticker,user_datetime,current_day)
currentDayEndPrice = 0
userEndPrice = 0

#This section retrieves the user's entered ticker historical financial information from Yahoo Finance.
data = requests.get(URL).text

#This section retrieves the most recent average of the high and low stock share price. 
try:
	#This first section is parsing through the text to retrieve the most recent high and low stock share price.
	firstSplit = data.split("HistoricalPriceStore")[1] 
	currentDaySplit = firstSplit.split("date")[1]
	currentDayHigh = currentDaySplit.split("high")[1] #Get the most recent high stock share price.
	currentDayLow = currentDaySplit.split("low")[1] #Get the most recent low stock share price.
	currentDayHighPrice = currentDayHigh.split(",")[0].strip("\"").strip(":") #Removes commas, quotation marks, and colons from high share price.
	currentDayLowPrice = currentDayLow.split(",")[0].strip("\"").strip(":") #Removes commas, quotation marks, and colons from low share price.
	currentDayEndPrice = (float(currentDayHighPrice) + float(currentDayLowPrice))/2 #Retrieves the average by adding the high and low share price together and dividing by 2.
except:
	#If there is a problem retrieving the most recent average stock share price, this error statement will be printed below and program exits.
	print("{} has an issue with determing current stock's stock share price with ticker {}.".format(date1,ticker))
	sys.exit(1)

#This section retrieves average of the high and low stock share price for the user entered date.
try:
	#This first section is parsing through the text to retrieve the user selected high and low stock share price.
	firstSplit = data.split("HistoricalPriceStore")[1]
	userSplit = firstSplit.split(str(user_datetime))[1]
	userHigh = userSplit.split("high")[1] #Get user high stock share price.
	userLow = userSplit.split("low")[1] #Get user low stock share price.
	userHighPrice = userHigh.split(",")[0].strip("\"").strip(":") #Removes commas, quotation marks, and colons from high share price.
	userLowPrice = userLow.split(",")[0].strip("\"").strip(":") #Removes commas, quotation marks, and colons from low share price.
	userEndPrice = (float(userHighPrice) + float(userLowPrice))/2 #Retrieves the average by adding the high and low share price together and dividing by 2.
except:
	#If there is a problem retrieving the user's average stock share price, this error statement will be printed below and program exits.
	print("{} has an issue with determing user's stock share price with ticker {}.".format(date1,ticker))
	sys.exit(1)

#This section prints the results.
try:
	userCostBasis = userEndPrice * shares #Get user's cost basis.
	currentSharePrice = currentDayEndPrice * shares #Get current stock share value by mulitplying the current share price by number of user shares.
	profit = currentSharePrice - userCostBasis #Get profit by subtracting the current share price by the user cost basis.
	profit = fixProfit(profit) #Use the fixProfit method to fix the formatting of the profit.
	print("Total Gross Profit for {} for {} shares bought on {} is ${}.\n".format(ticker,shares,date1,profit))
	getProfitAfterTax(year,month,day,profit,ticker,shares) #Uses the getProfitAfterTax method to print estimated profit after taxes.
except:
	#If there is a problem retrieving the proft, this error statement will be printed below and program exits.
	print("ERROR! Profits not calculated correctly for ticker {}.".format(ticker))
	sys.exit(1)

##############################################################################################################################################################################################

#EOF

##############################################################################################################################################################################################
