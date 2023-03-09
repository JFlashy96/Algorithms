/*
n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split.

Example

For n = 3 and m = 10, the output should be
solution(n, m) = 9.
*/
#include <iostream>
using namespace std;

int solution(int m, int n);
int main() {
	std::cout << "The solution is " << solution(10,3);
}
int solution(int m, int n) {
	return m - (m%n);
}