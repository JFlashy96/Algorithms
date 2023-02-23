"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.
"""
def solution(cell1, cell2):
	return (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1])) % 2 == 0
print(solution(cell1 = "A1", cell2 = "C3"))
print(solution(cell1="A1", cell2="H3"))