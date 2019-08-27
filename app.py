from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def isDate(pDate):
	for ch in pDate:
		if ch.isdigit():
			return True
	return False

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
			print(date)
	except:
		moreDates = False
print(dates)
#//*[@id="GroupGrid"]/div[3]/div[1]/text()
#//*[@id="GroupGrid"]/div[3]/div[2]/text()
#//*[@id="GroupGrid"]/div[3]/div[3]/text()
#//*[@id="GroupGrid"]/div[3]/div[4]/text()
#//*[@id="GroupGrid"]/div[3]/div[5]/text()
#//*[@id="GroupGrid"]/div[3]/div[6]/text()