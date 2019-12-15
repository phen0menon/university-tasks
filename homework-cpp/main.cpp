#include <fstream>
#include <iostream>
#include "hw4/token.hpp"
#include "hw4/scanner.hpp"

int main() {
  const std::string input = R"(C:\Development\university-tasks\homework-cpp\hw4\input.txt)";
  const std::string output = R"(C:\Development\university-tasks\homework-cpp\hw4\output.txt)";
  std::ifstream ifile(input);
  std::ofstream ofile(output);

  Scanner scanner(ifile);
  Token token;
  do {
    token = scanner.getNextToken();
    std::cout << token << "\n";
    if (token.getType() == LexemType::ERROR) {
      std::cerr << "Error!";
    }
  } while (token.getType() != LexemType::ERROR && token.getType() != LexemType::EOFF);

  ifile.close();
  ofile.close();

  return 0;
}