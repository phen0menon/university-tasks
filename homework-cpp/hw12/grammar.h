#pragma once

#ifndef HW11_GRAMMAR_H
#define HW11_GRAMMAR_H

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <unordered_map>
#include <utility>
#include <map>
#include "ps_automaton.h"

inline const std::string EPSILON = "e";

inline std::set<std::string> EPS_SET({EPSILON});

std::ostream &operator<<(std::ostream &stream, const std::set<std::string> &terminals);

class Grammar {
private:
    std::set<std::string> notTerminals;

    std::set<std::string> terminals;

    std::unordered_map<std::string, std::vector<std::vector<std::string>>> grammar;

    std::map<std::string, std::map<std::string, std::set<PSAutomatonCell>>> saTable;

    std::map<std::string, std::set<std::string>> FIRSTForG;

    std::map<std::string, std::set<std::string>> FOLLOWForG;

    std::vector<std::pair<std::string, std::vector<std::string>>> enumeratedRules;

    std::string firstNonTerminal;

    bool initFIRSTWithTerminalsAndEpsilon();

    bool initFIRSTWithNonTerminals();

    bool initFOLLOW();

    bool calculateFOLLOW();

    bool isTerminal(const std::string &word);

    bool isNonTerminal(const std::string &word);


public:
    Grammar();

    ~Grammar();

    bool loadGrammar(std::istream &stream);

    void printFIRST(std::ostream &stream);

    void printFOLLOW(std::ostream &stream);

    std::set<std::string> FIRST(const std::vector<std::string> &);

    std::set<std::string> FOLLOW(const std::string &);

    bool buildSATable();

    void printSATable();

    bool parse(std::istream &stream);
};

std::ostream &operator<<(std::ostream &stream, const Grammar &g);


#endif //HW11_GRAMMAR_H
