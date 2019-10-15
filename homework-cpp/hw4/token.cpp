#include "token.hpp"

const std::unordered_map<LexemType, std::string> Token::tokenRepresentationDict{
    {LexemType::NUM,       "NUM"},
    {LexemType::CHR,       "CHR"},
    {LexemType::STR,       "STR"},
    {LexemType::ID,        "ID"},
    {LexemType::LPAR,      "LPAR"},
    {LexemType::RPAR,      "RPAR"},
    {LexemType::LBRACE,    "LBRACE"},
    {LexemType::RBRACE,    "RBRACE"},
    {LexemType::LBRACKET,  "LBRACKET"},
    {LexemType::RBRACKET,  "RBRACKET"},
    {LexemType::SEMICOLON, "SEMICOLON"},
    {LexemType::COMMA,     "COMMA"},
    {LexemType::COLON,     "COLON"},
    {LexemType::OPASSIGN,  "OPASSIGN"},
    {LexemType::OPPLUS,    "OPPLUS"},
    {LexemType::OPMINUS,   "OPMINUS"},
    {LexemType::OPMULT,    "OPMULT"},
    {LexemType::OPINC,     "OPINC"},
    {LexemType::OPEQ,      "OPEQ"},
    {LexemType::OPNE,      "OPNE"},
    {LexemType::OPLT,      "OPLT"},
    {LexemType::OPGT,      "OPGT"},
    {LexemType::OPLE,      "OPLE"},
    {LexemType::OPNOT,     "OPNOT"},
    {LexemType::OPOR,      "OPOR"},
    {LexemType::OPAND,     "OPAND"},
    {LexemType::KWINT,     "KWINT"},
    {LexemType::KWCHAR,    "KWCHAR"},
    {LexemType::KWIF,      "KWIF"},
    {LexemType::KWELSE,    "KWELSE"},
    {LexemType::KWSWITCH,  "KWSWITCH"},
    {LexemType::KWCASE,    "KWCASE"},
    {LexemType::KWWHILE,   "KWWHILE"},
    {LexemType::KWFOR,     "KWFOR"},
    {LexemType::KWRETURN,  "KWRETURN"},
    {LexemType::KWIN,      "KWIN"},
    {LexemType::KWOUT,     "KWOUT"},
    {LexemType::EOFF,      "EOF"},
    {LexemType::ERROR,     "ERROR"}
};

/**
 * Constructor that implies using for lexems without parameters
 * @param type Lexem Type
 */
Token::Token(LexemType type) : _type(type) {};

/**
 * Constructor that implies using for lexems with integer parameter
 * @param value Integer value of lexem
 */
Token::Token(int value) : _value(value), _type(LexemType::NUM) {};

/**
 * Constructor that implies using for lexems with stringified value
 * @param type Lexem Type
 * @param str Stringified value of lexem
 */
Token::Token(LexemType type, const std::string &str) : _type(type), _str(str) {};

/**
 * Constructor that implies using for lexems with type of char
 * @param c Char that will be represented as int
 */
Token::Token(char c) : _value(c), _type(LexemType::CHR) {}

/**
 * Token representation method.
 * The method gets current LexemType and current value.
 * @return Stringified representation of token-value pair
 */
std::string Token::toString() const {
  const auto iterator = tokenRepresentationDict.find(_type);
  if (_type == LexemType::CHR) {
    return "[" + iterator->second + ", '" +
           std::string(1, static_cast<char>(_value)) + "']";
  } else if (_type == LexemType::NUM) {
    return "[" + iterator->second + ", " + std::to_string(_value) + "]";
  }
  return "[" + iterator->second + ", \"" + _str + "\"]";
}

/**
 * Overridden operator << for printing out a lexem.
 * The printing format is declared in Token::toString()
 * @param out Ostream instance
 * @param t Token instance
 * @return Ostream instance for further expressions
 */
std::ostream &operator<<(std::ostream &out, const Token &t) {
  out << t.toString();
  return out;
};