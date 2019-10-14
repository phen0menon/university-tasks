#ifndef HOMEWORK_TOKEN_HPP
#define HOMEWORK_TOKEN_HPP

#include <string>
#include <unordered_map>

enum class LexemType {
  NUM,
  CHR,
  STR,
  ID,
  LPAR,
  RPAR,
  LBRACE,
  RBRACE,
  LBRACKET,
  RBRACKET,
  SEMICOLON,
  COMMA,
  COLON,
  OPASSIGN,
  OPPLUS,
  OPMINUS,
  OPMULT,
  OPINC,
  OPEQ,
  OPNE,
  OPLT,
  OPGT,
  OPLE,
  OPNOT,
  OPOR,
  OPAND,
  KWINT,
  KWCHAR,
  KWIF,
  KWELSE,
  KWSWITCH,
  KWCASE,
  KWWHILE,
  KWFOR,
  KWRETURN,
  KWIN,
  KWOUT,
  EOFF,
  ERROR
};

class Token {
private:
  LexemType _type;
  int _value;
  std::string _str;
public:
  Token(LexemType type, const std::string& str);
  Token(LexemType type);
  Token(int value);
  Token(char c);

  std::string toString();
  void print(std::ostream &ostream);

  LexemType getType() {
    return this->_type;
  }

  int getValue() {
    return this->_value;
  }

  std::string getStr() {
    return this->_str;
  }
};

#endif  //HOMEWORK_TOKEN_HPP
