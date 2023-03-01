"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
the output should be

solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
"""
def solution(matrix):
	r = len(matrix)
	c = len(matrix[0])
	row = []
	for i in range(r):
		row.append([])
		for j in range(c):
			l = -matrix[i][j]
			for x in [-1,0,1]:
				for y in [-1,0,1]:
					if 0 <= i+x < r and 0 <= j+y < c:
						l += matrix[i+x][j+y]
			row[i].append(l)
	return row
print(solution(matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]))

"""
Explanation of solution:
The rows of a matrix are represented by r = the length of the input matrix.
The columns of a matrix are represented by c = the length of the first element
	in the matrix.
For every row, get the inverse of each value. For each value, check adjacent values
 	by using [-1,0,1] for the x and y axis. 
For every element in a row, after the inverse of the orginal value has been stored, 
	loop through the adjacent values to search for a True value. False values will be
	added as well, but since False returns a value of 0 this won't affect the total. 
	However, if a True value is found, this will increment the value of l and
	represent the number of mines (True values) that are adjacent to the cell in the current
	iteration.
Once cell has checked the adjacent elements in the matrix for a True value, add this 
	result to the matrix array.
Once every value in the original matrix has been checked, return the new matrix.
"""