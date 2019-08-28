from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timezone,timedelta
import pytz
import urllib
import requests


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
driver = webdriver.Chrome()
driver.get("https://www.when2meet.com/?8030438-YXUhk")

"""
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

dates = ['Aug 29', 'Aug 30', 'Aug 31', 'Sep 1', 'Sep 2']
times = ['9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM']
print(dates)
print(times)

start_time = datetime.strptime((dates[0] + ' ' + str(getYear(dates[0],times[0])) + '  ' + times[0]), '%b %d %Y %I %p')
start_time += timedelta(microseconds=0)
print(start_time.isoformat('T')+ "Z") 
"""
element = driver.find_element_by_xpath(('//*[@id="name"]'))
element.send_keys("Ethan Bensman")
#element.sendKeys("Ethan Bensman")//*[@id="SignIn"]/div/div/input
element = driver.find_element_by_xpath('//*[@id="SignIn"]/div/div/input')
element.click()


url = "https://www.when2meet.com/?8030438-YXUhk"
r = requests.get(url)
bsObj = BeautifulSoup(r.text, "html.parser")
cells = [x.get("id") for x in bsObj.findAll("div", id=lambda x: x and x.startswith('YouTime'))]


#for cell in cells:
	#print(cell)
	#print(type(cell))
	#print(cell.get('id'))
	#break



#//*[@id="YouTime1567083600"]		//*[@id="YouTime1567170000"]	//*[@id="YouTime1567256400"]
#//*[@id="YouTime1567084500"]
#//*[@id="YouTime1567085400"]
#//*[@id="YouTime1567086300"]
#//*[@id="YouTime1567087200"]
#//*[@id="YouTime1567088100"]
#//*[@id="YouTime1567089000"]
#
#
#
#
#
#
#
#
#
#
#
#






