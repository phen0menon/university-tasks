#ifndef HOMEWORK_SCANNER_H
#define HOMEWORK_SCANNER_H

#include <unordered_map>
#include "token.hpp"

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

class Scanner {

};


#endif //HOMEWORK_SCANNER_H
