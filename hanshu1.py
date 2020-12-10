
def chufa(a,b):
	if isinstance(a,(int,float,complex)):
		if isinstance(b,(int,float,complex)):
			if b==0:
				return "b shouldn't be 0"
			else:
				print(a/b)
		else:
			return None
	else:
		return None
print(chufa(1,0))
"""

def div(a,b):
	if not isinstance(a,(int,float)):
		return None
	if not isinstance(b,(int,float)):
		return None
	if b == 0:
		return None
	return a/b
print(div(1,0))
"""