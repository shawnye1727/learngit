s='I am a 19 years old boy! 666!'
def count_digits_in_a_sentence(s):
	if not isinstance(s,str):
		print('the sentence is not a unicode string')
		return 0
	result = 0
	for i in s:
		if i in '0123456789':
			result+=1
	return result

print(count_digits_in_a_sentence(s))

def count_words(s):
	if not isinstance(s,str):
		print('the sentence is not a unicode string')
	result = 0
	for i in s:
		if i in 'abcdefghigklmnopqrstuvwxyz':
			result+=1
	return result

print(count_words(s))

print(count_words(s)+count_digits_in_a_sentence(s))

def count_non_alphabetnum_in_a_sentence(s):
	count = len(s)
	return count-(count_words(s)+count_digits_in_a_sentence(s))