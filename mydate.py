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
	def inDate(self,start,end):
		if start > self.start and start < self.end:
			return True
		if end >self.start and end < self.end:
			return True
		else:
			return False


