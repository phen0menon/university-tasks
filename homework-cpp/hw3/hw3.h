#ifndef HW3_H
#define HW3_H

#include <string>
#include <vector>

// Task 1 - 2
int toDecimal(const std::string& num, int base);
std::string fromDecimal(int num, int base);

// Task 3
std::vector<std::string> split(const std::string& str, char delimiter);

// Task 4
void swap(int& a, int& b);
void sortIntegers(std::vector<int>& vec);

#endif // !HW3_H
