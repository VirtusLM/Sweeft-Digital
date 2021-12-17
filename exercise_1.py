
from collections import Counter

try:
	# Number input
	n = int(input("Enter the number of words [1 - 10^5] : "))
	if not 1 <= n <= 10**5:
		raise ValueError("Incorrect number")

	word_list = []
	# Word input
	for word in range(n):
		word = input("Enter the word (Lowercase English letters) : ")
		if word.islower() and word.isalpha():	# Checks words             
			word_list.append(word)
		else:
			raise ValueError("Incorrect letters")

	# Checks the sum of lengths of the words		
	if len(''.join(word_list)) > 10**6:		
		raise ValueError("The sum of the lengths of the words is greater than 10^6")

	# Counter
	print(len(Counter(word_list)))		
	for i in Counter(word_list).values():	
		print(i, end=' ')

except ValueError as e:
	print(e)
except Exception as e:
	print(e)



