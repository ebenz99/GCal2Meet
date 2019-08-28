from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timezone
import pytz


def isDate(pDate):
	for ch in pDate:
		if ch.isdigit():
			return True
	return False

def getYear(date, time):
	year = datetime.now().year
	if datetime.now() > datetime.strptime((dates[0] + ' ' + str(year) + '  ' + times[0]), '%b %d %Y %I %p'):
		year += 1
	return year
"""
driver = webdriver.Chrome()
driver.get("https://www.when2meet.com/?8030438-YXUhk")

moreDates = True
i = 1
dates = []

while moreDates:
	try:
		element = driver.find_element_by_xpath(('//*[@id="GroupGrid"]/div[3]/div[' + str(i) +']'))
		block = element.text
		date = (block.split("\n"))[0]
		i+=1
		if isDate(date):
			dates.append(date)
	except:
		moreDates = False

moreTimes = True
i = 4
times = []
while moreTimes:
	try:
		element = driver.find_element_by_xpath(('//*[@id="GroupGrid"]/div[2]/div['+str(i)+']/div/div'))
		block = element.text
		time = (block.split("M"))[0]+"M"
		if "Noon" in time:
			time = "12 PM"
		i+=4
		times.append(time)
	except:
		moreTimes = False

print(dates)
print(times)
"""

dates = ['Aug 29', 'Aug 30', 'Aug 31', 'Sep 1', 'Sep 2']
times = ['9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM']
print(dates)
print(times)

start_time = datetime.strptime((dates[0] + ' ' + str(getYear(dates[0],times[0])) + '  ' + times[0]), '%b %d %Y %I %p')
print(start_time)
print(start_time.replace(tzinfo=pytz.UTC))
print(start_time.replace(tzinfo=pytz.UTC).isoformat('T')+ "Z") 

#xpath of times - //*[(@id = "GroupGrid")]//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//div//div//div

#//*[@id="GroupGrid"]/div[2]/div[4]/div/div
#//*[@id="GroupGrid"]/div[2]/div[8]/div/div



