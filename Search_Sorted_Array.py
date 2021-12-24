"""
	Binary Search for an aelement in a rotated array.
	Big O is O(log n)
	The choice of the next element on which to perform some action
	is one of several possibilities. And only one will need to be 
	chosen. Or the elements on which the action is performed are digits of n.
	Example: Searching for a person in a contact list. Perform divide and conquer 
	to search for their name alphabetically and in every section only explore a subset
	of each section before eventually finding the correct contact.
"""
def search_sorted_array(l, n):
	a = ""
	if n in l:
		return (l.index(n))
	return -1

a = [5, 6, 7, 8, 9, 10, 1, 2, 3]
a_key = 10

b = [3, 5, 1, 2]
b_key = 6
 
print(search_sorted_array(a, a_key))
print(search_sorted_array(b, b_key))