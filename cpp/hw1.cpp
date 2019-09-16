#include <cmath>
#include <iostream>
#include <unordered_map>
#include <map>
#include <functional>

using UserChoiceHandler = std::function<void(int)>;

// task 1
bool isPrime(int number) {
	for (int i = 2; i <= sqrt(number); ++i) {
		if (number % i == 0) {
			return 0;
		}
	}
	return 1;
}

void printIsPrime(int number) {
	std::cout << isPrime(number) << "\n";
}

// task 2
void printPrimes(int count) {
	for (int i = 1; i <= count; ++i) {
		if (isPrime(i)) {
			std::cout << i << "\n";
		}
	}
}

// task 3
void printPrimesReversed(int count) {
	for (int i = count; i > 0; --i) {
		if (isPrime(i)) {
			std::cout << i << "\n";
		}
	}
}

// task 4
void printBinary(int decNum) {
	if (decNum / 2 != 0) {
		printBinary(decNum / 2);
	}
	std::cout << decNum % 2;
}


// task 5
UserChoiceHandler getUserChoiceHandler(int choice) {
	static const std::map<int, UserChoiceHandler> choices{
		{ 1, &printIsPrime },
		{ 2, &printPrimes },
		{ 3, &printPrimesReversed },
		{ 4, &printBinary },
	};
	auto iter = choices.find(choice);
	if (iter != choices.end()) {
		return iter->second;
	}
	return nullptr;
}

void execMenu() {
	int userChoice, input;
	std::cout << "Enter a number from 1 to 4: ";
	std::cin >> userChoice;
	std::cout << "Enter an input number: ";
	std::cin >> input;

	auto fn = getUserChoiceHandler(userChoice);
	if (fn == nullptr) {
		std::cout << "Not found handler for case " << userChoice << " case\n";
	}
	else {
		fn(input);
	}
}

int main() {
	execMenu();
	system("pause");
	return 0;
}
