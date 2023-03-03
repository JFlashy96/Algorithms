/*
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
solution(n) = 99.
*/
#include <iostream>
#include <cmath>
using namespace std;

int solution(int n);
int main() {
	std::cout << "The solution is " << solution(2);
}
int solution(int n) {
	return (int)pow(10,n)-1;
}