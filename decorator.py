# class A:
#     def add(self,x):
#         y = x + 1
#         print(y)

# class B(A):
# 	def add(self,x):
# 		super().add(x)

# if __name__ == "__main__":
# 	b = B()
# 	print(b.add(2))

from functools import wraps

def decorator(func):
	@wraps(func)
	def wrapTheFunction():
		print("before func to do something")
		func()
		print("after func to do something")
	return wrapTheFunction

@decorator
def a_function_requiring_decoration(one,two):
	result = one + two
	print(f"function {one} + {two} = ")

# @decorator == a_function_requiring_decoration = decorator(a_function_requiring_decoration)

a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)
