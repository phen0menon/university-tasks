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
  int _value;
  LexemType _type;
  std::string _str;

public:
  friend std::ostream &operator<<(std::ostream &out, const Token &t);

  static const std::unordered_map<LexemType, std::string> tokenRepresentationDict;

  std::string toString() const;

  Token(LexemType type, const std::string &str);

  Token(LexemType type);

  Token(int value);

  Token(char c);

  Token();

  inline LexemType getType() {
    return this->_type;
  }

  inline int getValue() {
    return this->_value;
  }

  inline std::string getStr() {
    return this->_str;
  }
};

#endif  //HOMEWORK_TOKEN_HPP
