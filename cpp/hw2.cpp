#include <vector>
#include <algorithm>
#include <iostream>
#include <conio.h>

// Task 2.1
int getIndexMin(std::vector<float> arr) {
	return std::distance(arr.begin(), std::min_element(arr.begin(), arr.end()));
}

// Task 2.2
std::vector<int> range(unsigned int end) {
	std::vector<int> rangeT;
	for (unsigned int i = 1; i <= end; i++) {
		int summary = 0;
		for (unsigned int j = 0; j < i; j++) {
			summary += (int) std::pow(i + j, 2);
		}
		rangeT.push_back(summary);
	}
	return rangeT;
}

// Task 2.3
bool isPalyndrome(std::vector<int> arr) {
	unsigned const arrSize = arr.size();
	for (unsigned int i = 0; i <= arrSize / 2; i++) {
		if (arr[i] != arr[arrSize - i - 1]) {
			return false;
		}
	}
	return true;
}

// Task 2.4
std::vector<int> findDiff(std::vector<char> dna) {
	std::vector<int> temp(dna.size());
	for (unsigned int i = 0; i < dna.size(); i++) {
		int countOfG = std::count(dna.begin(), dna.begin() + i, 'G');
		int countOfC = std::count(dna.begin(), dna.begin() + i, 'C');
		temp[i] = countOfG - countOfC;
	}
	return temp;
}

// Util
void printVec(std::vector<int> arr) {
	for (auto val : arr) {
		std::cout << val << " ";
	}
}

int main() {
	_getch();
	return 0;
}