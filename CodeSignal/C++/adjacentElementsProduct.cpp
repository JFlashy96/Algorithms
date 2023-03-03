#include <vector>
#include <iostream>
#include <algorithm>
int solution(std::vector <int> inputArray);
int main() {
	std::vector <int> inputArray = {3, 6, -2, -5, 7, 3};
	std::cout << "The solution is " << solution(inputArray); 
}
int solution(std::vector <int> inputArray) {
	int ans = -987654321;
	for (int i = 1; i < inputArray.size(); i++) {
		ans = std::max(ans, inputArray[i] * inputArray[i-1]);
	}
	return ans;
}