
try:
	# Returns grids on defined seconds
	def bomber_man(n, row, column, initial):
		full = [['O'] * column for i in range(row)]
		if n % 2 == 0:
			return full
		elif n % 4 == 1:
			return initial
		else:
			return detonation(row, column, initial, full)

	# Detonates bomb and 4 cells around	
	def detonation(row, column, initial, full):
		for x in range(row):
			for y in range(column):
				if initial[x][y] == 'O':
					full[x][y] = '.'
					# up
					if x - 1 >= 0:
						full[x-1][y] = '.'
					# down
					if x + 1 <= row - 1:
						full[x+1][y] = '.'
					# left
					if y - 1 >= 0:
						full[x][y-1] = '.'
					# right
					if y + 1 <= column - 1:
						full[x][y+1] = '.'
		return full

	# Time input	
	n = int(input("Enter the number of seconds: "))
	if n <= 0:
		raise ValueError("Incorrect number")

	grid = [ 
	      '.......', 
	      '...O...', 
	      '....O..', 
	      '.......', 
	      'OO.....', 
	      'OO.....'
      	]
   
	row = len(grid) 
	column = len(grid[0])  

	func = bomber_man(n, row, column, grid)
	for i in func:
		print(''.join(i))

except ValueError as e:
	print(e)
except Exception as e:
	print(e)
