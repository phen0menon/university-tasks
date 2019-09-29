#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>

// Task 1 ~ 2
std::string fromDecimal(int num, int base) {
  // if either base or num is invalid, return 0
  if (base < 2 || base > 36 || num == 0) {
    return "0";
  }
  // if num is negative, make it positive
  if (num < 0) num *= -1;
   
  std::string out;
  while (num > 0) {
    char digit = num % base;
    digit += digit < 10 ? '0' : 'A' - 10;
    out += digit;
    num /= base;
  }
  std::reverse(out.begin(), out.end());
  return out;
}

int toDecimal(const std::string& num, int base) {
  // if base is invalid, return 0
  if (base < 2 || base > 36) {
    return 0;
  }

  int out = 0;
  for (int i = num.length() - 1, digValue = 1; i >= 0; --i, digValue *= base) {
    char s = static_cast<unsigned char>(std::toupper(num[i]));
    char nextDig = isdigit(s) ? s - '0' : s - 'A' + 10;

    if (nextDig >= base) {
      return 0;
    }

    out += nextDig * digValue;
  }
  return out;
}

void testDecimal() {
  int original = 128;
  int base = 11;
  std::cout << original << " " << base << "\n";
  std::string a = fromDecimal(original, base);
  std::cout << a << "\n";
  int next = toDecimal(a, base);
  std::cout << next;
}


// Task 3
void printVector(std::vector<std::string> arr) {
  for (auto it = arr.begin(); it < arr.end(); ++it)
    std::cout << *it << std::endl;
}

std::vector<std::string> split(const std::string &str, char delimiter) {
  std::vector<std::string> out;
  std::istringstream iss(str);
  std::string token;
  while (std::getline(iss, token, ' ')) {
    out.push_back(token);
  }
  return out;
}

// Task 4
void swap(int& a, int& b) {
  int t = a;
  a = b;
  b = t;
}

void sortIntegers(std::vector<int> &vec) {
  for (int i = 0; i < vec.size(); i++) {
    for (int j = 0; j < vec.size() - i - 1; j++) {
      if (vec[j] > vec[j + 1]) 
        swap(vec[j], vec[j + 1]);
    }
  }
}

int main() {
  return 0;
}