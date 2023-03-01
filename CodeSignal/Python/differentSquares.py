"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
solution(matrix) = 6.
"""
def solution(matrix):
	s = set()
	for i in range(0, len(matrix)-1):
		for j in range(0, len(matrix[i])-1):
			s.add((matrix[i+1][j], matrix[i+1][j+1], matrix[i][j], matrix[i][j+1]))
	return len(s)
print(solution(matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]))