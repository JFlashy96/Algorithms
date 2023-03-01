/*
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.
*/

#include <string>
#include <iostream>
 
bool valid(int a, int b);
int solution(std::string cell);
int main() {
	std::cout << "The solution is " << solution("a1");
}
bool valid(int a, int b) {
	return a >= 0 && a < 8 && b >= 0 && b < 8;
}
int solution(std::string cell) {
	int a  = cell.front() - 'a', b = cell.back() - '1';
	return valid(a-2,b-1)
		+ valid(a-2,b+1)
		+ valid(a+2,b-1)
		+ valid(a+2,b+1)
		+ valid(a-1,b-2)
		+ valid(a-1,b+2)
		+ valid(a+1,b-2)
		+ valid(a+1,b+2)
	;
}