"""
	Prints the last 10 lines of a file.
"""
def print_n_last_lines(n):
	"""
		Print the last n lines of a file.
	"""
	with open("file.txt") as f:
		lines = f.readlines()
		lines = [line.rstrip() for line in lines]
		print(lines[-n:len(lines)])
print_n_last_lines(10)
