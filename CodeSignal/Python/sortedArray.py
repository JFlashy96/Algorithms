def sortedArray(n, arr):

	l_bound = 0
	r_bound = n - 1 
	i = 0

	while i <= r_bound:
		if arr[i] == 2:
			arr[i] = arr[r_bound]
			arr[r_bound] = 2
			r_bound -= 1
		elif arr[i] == 1:
			i += 1
		else: 
			arr[i] = arr[l_bound]
			arr[l_bound] = 0
			l_bound += 1
			i += 1
	return arr 

n = int(input())
arr = list(map(int, input().split()))
print("The solution is {}".format(sortedArray(n, arr)))