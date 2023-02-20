"""
	Jonathan Alston
	January 2022
	Write a function to crush candy in one dimensional board. In candy crushing games, 
	groups of like items are removed from the board. In this problem, any sequence of 3 
	or more like items should be removed and any items adjacent to that sequence should
	now be considered adjacent to each other. This process should be repeated as many 
	time as possible. You should greedily remove characters from left to right.
"""
def candy_crush(input):
	if not input:
		return input

	stack = []
	stack.append([input[0],1])

	for i in range(1, len(input)):
		if input[i] != input[i-1]:
			if stack[-1][1] >= 3:
				print("greater than or equal to 3. {}".format(stack[-1][1]))
				stack.pop()
				print(stack)
			if stack and stack[-1][0] == input[i]:
				print("this is stack[-1][0] {}".format(stack[-1][0]))
				print("this is stack[-1][1] before incrementing {}".format(stack[-1][1]))
				stack[-1][1] += 1
				print("this is stack[-1][1] after incrementing {}".format(stack[-1][1]))
			else:
				stack.append([input[i], 1])
		else:
			print("characters are equal. {}".format(stack[-1][1]))
			stack[-1][1] += 1
			print("after incrementing. {}".format(stack[-1][1]))

	# handle end
	if stack[-1][1] >= 3:
		stack.pop()

	out = []
	for ltrs in stack:
		out += ltrs[0] * ltrs[1]

	return ''.join(out)

print(candy_crush("aaaabbbc")) #cf
