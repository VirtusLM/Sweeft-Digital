
try:
	# Number input
	T = int(input("Enter the number of test cases [1 - 10^5] : "))
	if not 1 <= T <= 10**5:
		raise ValueError("Incorrect number")

	word_list = []
	# Word input
	for w in range(T):
		w = input("Enter the word (Lowercase English letters) : ")
		if w.islower() and w.isalpha() and 1 <= len(w) <= 100:             
			word_list.append(w)
		else:
			raise ValueError("Incorrect letters")

	# Compares letters and divides
	def compare(ls):
		if len(ls) == 1:  
			return False
		elif ls[-1] > ls[-2]:
			return (ls[:-1])  
		else:
			return compare(ls[:-1])  

	# Checks and sorts
	for w in word_list:
		w = list(w)
		list_one = compare(w)
		if not list_one:  
			print("no answer")
			continue      
		list_two = w[len(list_one):]  
		list_two.sort()  

		# Swaps letters
		for index, item  in enumerate(list_two):  
			if list_one[-1] < item:
				a = list_two.pop(index) 
				b = list_one.pop(-1) 
				list_two.insert(index, b)  
				list_one.append(a) 
				break

		print(''.join(list_one + list_two))

except ValueError as e:
	print(e)
except Exception as e:
	print(e)
