class ClassTest(object):
	"""docstring for ClassTest"""
	__num = 0

	@classmethod
	def addNum(cls):
		cls.__num += 1

	@classmethod
	def getNum(cls):
		return cls.__num

	def __new__(self):
		ClassTest.addNum()
		return super(ClassTest,self).__new__(self)

class Student(ClassTest):
	"""docstring for Student"""
	def __init__(self):
		self.name = ""

if __name__ == "__main__":
    a = Student()
    b = Student()
    print(ClassTest.getNum())		