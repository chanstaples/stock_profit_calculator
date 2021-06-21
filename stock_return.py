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
import webbrowser

##############################################################################################################################################################################################

#Script Execution Section

#This section retrieves user information.
ticker = get_ticker()
year = get_user_year(ticker)
month = get_user_month(ticker,year)
day = get_user_day(ticker,year,month)
date1 = "{}-{}-{}".format(month,day,year)
shares = get_user_shares(ticker,date1)
print("Beginning calculation.\n")
user_datetime = getStartDateTime(date1)
current_day = datetime.now().timestamp()
current_day = int(current_day)

#This section prepares program to retrieve information from Yahoo Finance.
URL="https://finance.yahoo.com/quote/{}/history?period1={}&period2={}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true".format(ticker,user_datetime,current_day)
currentDayEndPrice = 0
userEndPrice = 0

#This section retrieves information from Yahoo Finance.
data = requests.get(URL).text

#This section retrieves the most recent average of the high and low stock share price.
try:
	firstSplit = data.split("HistoricalPriceStore")[1]
	currentDaySplit = firstSplit.split("date")[1]
	currentDayHigh = currentDaySplit.split("high")[1]
	currentDayLow = currentDaySplit.split("low")[1]
	currentDayHighPrice = currentDayHigh.split(",")[0].strip("\"").strip(":")
	currentDayLowPrice = currentDayLow.split(",")[0].strip("\"").strip(":")
	currentDayEndPrice = (float(currentDayHighPrice) + float(currentDayLowPrice))/2
except:
	print("{} has an issue with determing current stock's stock share price with ticker {}.".format(date1,ticker))

#This section retrieves the user selected average of the high and low stock share price.
try:
	firstSplit = data.split("HistoricalPriceStore")[1]
	print(firstSplit)
	print(user_datetime)
	userSplit = firstSplit.split(str(user_datetime))[1]
	userHigh = userSplit.split("high")[1]
	userLow = userSplit.split("low")[1]
	userHighPrice = userHigh.split(",")[0].strip("\"").strip(":")
	userLowPrice = userLow.split(",")[0].strip("\"").strip(":")
	userEndPrice = (float(userHighPrice) + float(userLowPrice))/2
except:
	print("{} has an issue with determing user's stock share price with ticker {}.".format(date1,ticker))

#This section prints the results.
try:
	userSharePrice = userEndPrice * shares
	currentSharePrice = currentDayEndPrice * shares
	profit = currentSharePrice - userSharePrice
	profit = fixProfit(profit)
	print("Total Gross Profit for {} for {} shares bought on {} is ${}.\n".format(ticker,shares,date1,profit))
	getProfitAfterTax(year,month,day,profit,ticker,shares)
except:
	print("ERROR! Profits not calculated correctly for ticker {}.".format(ticker))

##############################################################################################################################################################################################

#EOF

##############################################################################################################################################################################################
