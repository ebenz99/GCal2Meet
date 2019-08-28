from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
#import pytz
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timezone,timedelta
import requests
import mydate

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
name = 'Ethan Bensman'


def isDate(pDate):
	for ch in pDate:
		if ch.isdigit():
			return True
	return False

def getYear(date, time):
	year = datetime.now().year
	if datetime.now() > datetime.strptime((date + ' ' + str(year) + '  ' + time), '%b %d %Y %I %p'):
		year += 1
	return year

def getEvents(dates,times):
	"""Shows basic usage of the Google Calendar API.
	Prints the start and name of the next 10 events on the user's calendar.
	"""
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('calendar', 'v3', credentials=creds)

	start_time = (datetime.strptime((dates[0] + ' ' + str(getYear(dates[0],times[0])) + '  ' + times[0]), '%b %d %Y %I %p')).isoformat('T')+ "Z"
	end_time = (datetime.strptime((dates[len(dates)-1] + ' ' + str(getYear(dates[len(dates)-1],times[len(dates)-1])) + '  ' + times[len(times)-1]), '%b %d %Y %I %p')+timedelta(days=1)).isoformat('T')+ "Z"
	#end_time = (datetime.strptime((dates[len(dates)-1] + ' ' + str(getYear(dates[len(dates)-1],times[len(dates)-1])) + '  11 PM'), '%b %d %Y %I %p')).isoformat('T')+ "Z"


	# Call the Calendar API
	#now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	events_result = service.events().list(calendarId='primary', timeMin=start_time, timeMax=end_time,
										singleEvents=True,
										orderBy='startTime').execute()
	events = events_result.get('items', [])

	if not events:
		print('No upcoming events found.')
	rlist = []
	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date'))
		end = event['end'].get('dateTime', event['end'].get('date'))
		print(start, end, event['summary'])
		if len(start) < 11:
			rlist.append(event)
	print("RLIST LEN IS")
	print(len(rlist))
	for event in rlist:
		events.remove(event)
	return events

def main():
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



	events = getEvents(dates,times)
	myEvents = []
	for event in events:
		startstr = event['start'].get('dateTime', event['start'].get('date'))
		#print(startstr)
		endstr = event['end'].get('dateTime', event['end'].get('date'))
		start = datetime.strptime(startstr, '%Y-%m-%dT%H:%M:%f%z').replace(tzinfo=None)
		end = datetime.strptime(endstr, '%Y-%m-%dT%H:%M:%f%z').replace(tzinfo=None)
		myEvents.append(mydate.myDate(start,end))

	
	element = driver.find_element_by_xpath(('//*[@id="name"]'))
	element.send_keys(name)
	element = driver.find_element_by_xpath('//*[@id="SignIn"]/div/div/input')
	element.click()


	url = "https://www.when2meet.com/?8030438-YXUhk"
	r = requests.get(url)
	bsObj = BeautifulSoup(r.text, "html.parser")
	cells = [x.get("id") for x in bsObj.findAll("div", id=lambda x: x and x.startswith('YouTime'))]

	grid = [[] for date in dates]
	print(grid)

	for idx,cell in enumerate(cells):
		grid[idx%len(dates)].append(cell)
	
	dic = {}

	for rIdx, row in enumerate(grid):
		for cIdx, num in enumerate(row):
			starttime = (datetime.strptime((dates[rIdx] + ' ' + str(getYear(dates[rIdx],times[0])) + '  ' + times[0]), '%b %d %Y %I %p') + timedelta(minutes=15*cIdx))
			endtime = (starttime + timedelta(minutes=15))
			dic[num] = True
			for myEvent in myEvents:
				if myEvent.inDate(starttime,endtime) == True:
					dic[num] = False

	print(dic)


	for element in dic.keys():
		if dic[element] == True:
			el = driver.find_element_by_xpath(('//*[@id="' + element + '"]'))
			el.click()

	while True:
		pass

if __name__ == "__main__":
	main()
