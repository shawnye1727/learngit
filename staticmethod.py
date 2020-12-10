import time
class TimeTest(object):
	"""docstring for TimeTest"""
	def __init__(self, hour, minute, second):
		#super(TimeTest, self).__init__()
		self.hour = hour
		self.minute = minute
		self.second = second

	@staticmethod
	def showTime():
		return time.strftime("%H-%M-%S",time.localtime())

	def showClassTime(self):
		classtime = "{}:{}:{}".format(self.hour,self.minute,self.second)
		return classtime

# if __name__ == "__main__":
# 	print(TimeTest.showTime())
# 	t = TimeTest(12,12,12)
# 	print(t.showTime())

#无需实例化，直接调用类的静态方法
print(TimeTest.showTime())

#实例化后，也可以直接调用类的静态方法
t = TimeTest(1,2,3)
print(t.showTime())
#实例化后，调用成员方法
print(t.showClassTime())
