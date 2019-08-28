import datetime 
class myDate:
	def __init__(self,start,end):
		self.start = start - datetime.timedelta(minutes=15)
		self.end = end + datetime.timedelta(minutes=15)
	def tryCombine(self,second):
		if self.end > second.start:
			return myDate(self.start,second.end)
		else:
			None
	def inDate(start,end):
		if time.start > self.start and time.start < self.end:
			return True
		elif time.end >self.start and time.end < self.end:
			return True
		else:
			return False


