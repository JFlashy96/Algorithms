import algo_timer as alt
from random import randint

array = [3,5,6,2,4,7]

def bubble_sort(array):
	n = len(array)

	for i in range(n):

		already_sorted = True

		for j in range(n - i - 1):
			# sorts in ascending order
			if array[j] > array[j + 1]:

				array[j], array[j + 1] = array[j + 1], array[j]

				already_sorted = False

		if already_sorted:
			break

	return array 

print(array)
array = bubble_sort(array)
print(array)

if __name__ == "__main__":

	ARRAY_LENGTH = 10000
	array = [randint(0,1000) for i in range(ARRAY_LENGTH)]

	alt.run_sorting_algorithm(algorithm="bubble_sort", array=array)
#	alt.run_sorting_algorithm(algorithm="insertion_sort", array=array)