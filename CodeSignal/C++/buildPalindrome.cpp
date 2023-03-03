/*
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".
*/
#include <string>
#include <iostream>

std::string solution(std::string st);
bool isPalindrome(std::string st);
int main() {
	std::cout << "The solution is " << solution("abcdcba");
}
std::string solution(std::string st) {
	if (isPalindrome(st)) return st;
	return st[0] + solution(st.substr(1)) + st[0];
}
bool isPalindrome(std::string st) {
	if (st.length() == 0 || st.length() == 1) return true;
	return st[0] == st[st.length() -1] &&
		isPalindrome(st.substr(1, st.length()-2));	
}