#include <vector>
#include <iostream>
#include <string>
#include <cstring>

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



int main() {

  return 0;
}