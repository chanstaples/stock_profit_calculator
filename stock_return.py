import sys
import requests
import json
from datetime import datetime
from datetime import date
from help import *
import webbrowser

ticker = get_ticker()
year = get_user_year(ticker)
month = get_user_month(ticker,year)
day = get_user_day(ticker,year,month)
date1 = "{}-{}-{}".format(month,day,year)
shares = get_user_shares(ticker,date1)
print("Beginning calculation.\n")
user_datetime = getStartDateTime(date1)
second_user_datetime = getStartDateTime2(date1)
current_day = datetime.now().timestamp()
current_day = int(current_day)

URL="https://finance.yahoo.com/quote/{}/history?period1={}&period2={}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true".format(ticker,user_datetime,current_day)
#webbrowser.open(URL)
currentDayEndPrice = 0
userEndPrice = 0

try:
	data = requests.get(URL).text
	firstSplit = data.split(str(user_datetime))[9]
	secondSplit = firstSplit.split("HistoricalPriceStore")[1]
	currentDaySplit = secondSplit.split("date")[1]
	currentDayHigh = currentDaySplit.split("high")[1]
	currentDayLow = currentDaySplit.split("low")[1]
	currentDayHighPrice = currentDayHigh.split(",")[0].strip("\"").strip(":")
	currentDayLowPrice = currentDayLow.split(",")[0].strip("\"").strip(":")
	currentDayEndPrice = (float(currentDayHighPrice) + float(currentDayLowPrice))/2
	thirdSplit = secondSplit.split(str(second_user_datetime))[1]
	userHigh = thirdSplit.split("high")[1]
	userLow = thirdSplit.split("low")[1]
	userHighPrice = userHigh.split(",")[0].strip("\"").strip(":")
	userLowPrice = userLow.split(",")[0].strip("\"").strip(":")
	userEndPrice = (float(userHighPrice) + float(userLowPrice))/2
except:
	print("{} has an issue with ticker {}.".format(date1,ticker))

try:
	userSharePrice = userEndPrice * shares
	currentSharePrice = currentDayEndPrice * shares
	profit = getProfit(userSharePrice,currentSharePrice)
	print("Total Gross Profit for {} for {} shares bought on {} is ${}.\n".format(ticker,shares,date1,profit))
except:
	print("ERROR! Profits not calculated correctly for ticker {}.".format(ticker))


