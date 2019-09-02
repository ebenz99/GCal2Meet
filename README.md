# GCal2Meet

A repository that automates filling out when2meet's with your google calendar.

## Directions

1. `pip3 install requirements.txt` - installs the necessary requirements to run
2. If you don't have it already, download the [chrome web driver](https://chromedriver.chromium.org/downloads) and add it to your PATH
3. [Enable the Google Calendar API](https://developers.google.com/calendar/quickstart/python) and move its `credentials.json` into your project folder
4. Change the variable `name` in controller.py to your own
5. Run with the command `python3 controller.py <when2meet URL>`

## Known Issue
1. If a When2Meet spans multiple years, it fills based on your calendar for the current year