#include <string>
#include <iostream>
int solution(int product);
int main() {
	std::cout << "The answer is " << solution(450);
}
int solution(int product) {
	if (product < 10) 
		return product ?: 10;
	std::string r;
	for (int i = 9; i > 1; i--) {
		while (product % i == 0) {
			product /= i;
			r = char('0' + i) + r;
		}
	}
	return product == 1 ? std::stoi(r) :-1;
}