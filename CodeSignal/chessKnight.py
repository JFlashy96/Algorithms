"""
Given a position of a knight on the standard chessboard, 
find the number of different moves the knight can perform.

For cell = "a1", the output should be
solution(cell) = 2.

For cell = "c2", the output should be
solution(cell) = 6
"""
def solution(cell):
	x,y = ord(cell[0])-96, int(cell[1])
	return sum([1 <= x+i <= 8 and 1 <= y+j <= 8 for i in [-2,-1,1,1] for j in [-2,-1,1,2]])//2
print(solution(cell="c2"))
print(solution(cell="a1"))