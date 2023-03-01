"""
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:

For bishop = "a1" and pawn = "c3", the output should be
solution(bishop, pawn) = true.

For bishop = "h1" and pawn = "h3", the output should be
solution(bishop, pawn) = false.
"""
def solution(bishop, pawn):
	bishop = (ord(bishop[0]), int(bishop[1]))
	pawn = (ord(pawn[0]), int(pawn[1]))
	return bishop[1]-bishop[0] == pawn[1]-pawn[0] or sum(bishop) == sum(pawn)
print(solution(bishop = "a1", pawn = "c3"))
print(solution(bishop = "h1", pawn = "h3"))