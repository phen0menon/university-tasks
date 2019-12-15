#ifndef HOMEWORK_SCANNER_HPP
#define HOMEWORK_SCANNER_HPP

#include <unordered_map>
#include <istream>
#include "token.hpp"

extern std::unordered_map<char, LexemType> separators;
extern std::unordered_map<std::string, LexemType> keywords;
extern std::unordered_map<std::string, LexemType> operators;

enum States {
  INITIAL,
  DIGIT,
  PROBCHAR,
  CHAR,
  PROBSTRING,
  STRING,
  MINUSORNEGATIVE,
  NEQORLOGICALNOT,
  COMP,
  EQORASSIGN,
  INCORPLUS,
  LOGICALOR,
  LOGICALAND,
};

class Scanner {
private:
  int number = 0;
  char character = '\0';
  std::string string = "";

  int currState = 0;
  char currCharacter = '\0';

  bool stop = false;
  bool stopCurrent = false;
  bool negNumber = false;

  Token end = Token(LexemType::EOFF);

  std::istream &is;

public:
  explicit Scanner(std::istream &is);

  Token getNextToken();
};



#endif //HOMEWORK_SCANNER_HPP
