"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
"""
def solution(a, b):
	r = []
	for i in range(0, len(a)):
		if a[i] != b[i]:
			# add the pair of mismtched elements to r
			r.append([a[i], b[i]])
	# True if lists match or there are most one pair of
	# elements whose values match
	if len(r) == 0 or len(r) == 2 and r[0] == r[1][::-1]:
		return True
	return False

# Driver code
a = [1, 2, 3]
b = [1, 2, 3]
print(solution(a, b))
a = [1, 2, 3]
b = [1, 2, 3]
print(solution(a, b))
a = [1, 2, 2]
b = [2, 1, 1]
print(solution(a, b))