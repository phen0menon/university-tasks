#include "scanner.hpp"

std::unordered_map<char, LexemType> separators{
    {'(', LexemType::LPAR},
    {')', LexemType::RPAR},
    {'[', LexemType::LBRACKET},
    {']', LexemType::RBRACKET},
    {'{', LexemType::LBRACE},
    {'}', LexemType::RBRACE},
    {';', LexemType::SEMICOLON},
    {',', LexemType::COMMA},
    {':', LexemType::COLON},
};

std::unordered_map<std::string, LexemType> keywords{
    {"return", LexemType::KWRETURN},
    {"int",    LexemType::KWINT},
    {"char",   LexemType::KWCHAR},
    {"if",     LexemType::KWIF},
    {"else",   LexemType::KWELSE},
    {"switch", LexemType::KWSWITCH},
    {"case",   LexemType::KWCASE},
    {"while",  LexemType::KWWHILE},
    {"for",    LexemType::KWFOR},
    {"in",     LexemType::KWIN},
    {"out",    LexemType::KWOUT}
};

std::unordered_map<std::string, LexemType> operators{
    {"=",  LexemType::OPASSIGN},
    {"+",  LexemType::OPPLUS},
    {"-",  LexemType::OPMINUS},
    {"*",  LexemType::OPMULT},
    {"++", LexemType::OPINC},
    {"==", LexemType::OPEQ},
    {"!=", LexemType::OPNE},
    {"<",  LexemType::OPLT},
    {">",  LexemType::OPGT},
    {"<=", LexemType::OPLE},
    {"!",  LexemType::OPNOT},
    {"||", LexemType::OPOR},
    {"&&", LexemType::OPAND}
};

bool isCharDigit(char c) {
  return '0' <= c && c <= '9';
}

int charToInt(char c) {
  return c - '0';
}

bool isCharLetter(char c) {
  return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || c == '_';
}

Scanner::Scanner(std::istream &is) : is(is) {}

Scanner &operator>>(Scanner &scanner, Token &token) {
  token = scanner.getNextToken();
  return scanner;
}

Token Scanner::getNextToken() {
  if (stop) {
    return end;
  }

  while (true) {
    if (!stopCurrent || is.eof()) {
      currCharacter = is.get();
      if (is.eof()) {
        if (currState == States::INITIAL) {
          stop = true;
          end = Token(LexemType::EOFF);
          return end;
        } else if ((currState == States::CHAR || currState == States::PROBSTRING || currState == States::LOGICALOR ||
                    currState == States::LOGICALAND)) {
          stop = true;
          end = Token(LexemType::ERROR, "unexpected EOF");
          return end;
        }
      }
    }
    stopCurrent = false;

    if (currState == States::INITIAL) {
      if (isCharDigit(currCharacter)) {
        currState = States::DIGIT;
        number = charToInt(currCharacter);
        continue;
      } else if (currCharacter == '*') {
        return Token(LexemType::OPMULT);
      } else if (separators.find(currCharacter) != separators.end()) {
        Token out(separators.find(currCharacter)->second);
        return out;
      } else if (currCharacter == ' ' || currCharacter == '\n') {
        continue;
      } else if (currCharacter == '\'') {
        currState = States::PROBCHAR;
        continue;
      } else if (currCharacter == '!') {
        currState = States::NEQORLOGICALNOT;
        continue;
      } else if (currCharacter == '<') {
        currState = States::COMP;
        continue;
      } else if (currCharacter == '=') {
        currState = States::EQORASSIGN;
        continue;
      } else if (currCharacter == '+') {
        currState = States::INCORPLUS;
        continue;
      } else if (currCharacter == '|') {
        currState = States::LOGICALOR;
        continue;
      } else if (currCharacter == '&') {
        currState = States::LOGICALAND;
        continue;
      } else if (currCharacter == '"') {
        currState = States::PROBSTRING;
        continue;
      } else if (isCharLetter(currCharacter)) {
        currState = States::STRING;
        string += currCharacter;
        continue;
      } else if (currCharacter == '-') {
        currState = States::MINUSORNEGATIVE;
        continue;
      } else if (currCharacter == '>') {
        return Token(LexemType::OPGT);
      }
    } else if (currState == States::DIGIT) {
      if (isCharDigit(currCharacter)) {
        if (negNumber) {
          number = number * States::INCORPLUS - charToInt(currCharacter);
        } else {
          number = number * States::INCORPLUS + charToInt(currCharacter);
        }
        continue;
      } else {
        Token out(number);
        currState = States::INITIAL;
        number = States::INITIAL;
        negNumber = false;
        stopCurrent = true;
        return out;
      }
    } else if (currState == States::PROBCHAR) {
      if (currCharacter == '\'') {
        stop = true;
        return Token(LexemType::ERROR, "empty chr");
      } else {
        currState = States::CHAR;
        character = currCharacter;
        continue;
      }
    } else if (currState == States::CHAR) {
      if (currCharacter == '\'') {
        Token out(character);
        currState = States::INITIAL;
        return out;
      } else {
        stop = true;
        end = Token(LexemType::ERROR, "invalid chr");
        return end;
      }
    } else if (currState == States::PROBSTRING) {
      if (currCharacter == '"') {
        Token out(LexemType::STR, string);
        currState = States::INITIAL;
        string = "";
        return out;
      } else {
        string += currCharacter;
        continue;
      }
    } else if (currState == States::STRING) {
      if (isCharLetter(currCharacter) || isCharDigit(currCharacter)) {
        string += currCharacter;
        continue;
      } else if (keywords.find(string) != keywords.end()) {
        Token out(keywords.find(string)->second);
        string = "";
        currState = States::INITIAL;
        stopCurrent = true;
        return out;
      } else {
        Token out(LexemType::ID, string);
        string = "";
        currState = States::INITIAL;
        stopCurrent = true;
        return out;
      }
    } else if (currState == States::MINUSORNEGATIVE) {
      if (isCharDigit(currCharacter)) {
        number = (-1) * charToInt(currCharacter);
        currState = States::DIGIT;
        negNumber = true;
        continue;
      } else {
        Token out(LexemType::OPMINUS);
        currState = States::INITIAL;
        stopCurrent = true;
        return out;
      }
    } else if (currState == States::NEQORLOGICALNOT) {
      if (currCharacter == '=') {
        Token out(LexemType::OPNE);
        currState = States::INITIAL;
        return out;
      } else {
        Token out(LexemType::OPNOT);
        currState = States::INITIAL;
        stopCurrent = true;
        return out;
      }
    } else if (currState == States::COMP) {
      if (currCharacter == '=') {
        Token out(LexemType::OPLE);
        currState = States::INITIAL;
        return out;
      } else {
        Token out(LexemType::OPLT);
        currState = States::INITIAL;
        stopCurrent = true;
        return out;
      }
    } else if (currState == States::EQORASSIGN) {
      if (currCharacter == '=') {
        Token out(LexemType::OPEQ);
        currState = States::INITIAL;
        return out;
      } else {
        Token out(LexemType::OPASSIGN);
        currState = States::INITIAL;
        stopCurrent = true;
        return out;
      }
    } else if (currState == States::INCORPLUS) {
      if (currCharacter == '+') {
        Token out(LexemType::OPINC);
        currState = States::INITIAL;
        return out;
      } else {
        Token out(LexemType::OPPLUS);
        currState = States::INITIAL;
        stopCurrent = true;
        return out;
      }
    } else if (currState == States::LOGICALOR) {
      if (currCharacter == '|') {
        Token out(LexemType::OPOR);
        currState = States::INITIAL;
        return out;
      } else {
        stop = true;
        end = Token(LexemType::ERROR, "expected ||");
        return end;
      }
    } else if (currState == States::LOGICALAND) {
      if (currCharacter == '&') {
        Token out(LexemType::OPAND);
        currState = States::INITIAL;
        return out;
      } else {
        stop = true;
        end = Token(LexemType::ERROR, "expected &&");
        return end;
      }
    }
    stop = true;
    std::string text = "unknown symbol ";
    text += currCharacter;
    end = Token(LexemType::ERROR, text);
    return end;
  }
}