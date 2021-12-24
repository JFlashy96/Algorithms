"""
	Time complexity for binary heap:
		Insertion: O(log(n))
		Deletion: O(log(n))
"""

"""
	In heap structures the purpose is to keep the strucuture maintained at time of insertion/deletion
	so that the first element of the structure will always be the smallest.
"""
import algo_timer as alt
import heapq

li = [5,7,9,1,3]

# using heapify to convert list into heap
heapq.heapify(li)

print("The created heap is: ",end="")
print(list(li))

heapq.heappush(li, 4)

print("The modified heap after push is: ",end="")
print(list(li))

print("The popped and smallest element is: ",end="")
print(heapq.heappop(li))

def max_heapify(A,k):
	l = left(k)
	r = right(k)

	if l < len(A) and A[l] > A[k]:
		largest = l
	else:
		largest = k
	if r < len(A) and A[r] > A[largest]:
		largest = r
	if largest != k:
		A[k], A[largest] = A[largest], A[k]
		max_heapify(A,largest)

def min_heapify(A,k):
	l = left(k)
	r = right(k)

	if l < len(A) and A[l] < A[k]:
		smallest = l
	else:
		smallest = k
	if r < len(A) and A[r] < A[smallest]:
		smallest = r
	if smallest != k:
		A[k], A[smallest] = A[smallest], A[k]
		min_heapify(A, smallest)

def left(k):
	return 2 * k + 1

def right(k):
	return 2 * k + 2

def build_max_heap(A):
	n = int((len(A)/2)-1)
	for k in range(n,-1,-1):
		max_heapify(A,k)

def build_min_heap(A):
	n = int((len(A)/2)-1)
	for k in range(n, -1, -1):
		min_heapify(A,k)

A = [3,9,2,1,4,5]
print(A)
build_max_heap(A)
print(A)
build_min_heap(A)
print(A)



