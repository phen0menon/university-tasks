//
// Created by phen0menon on 18.04.2020.
//
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

std::set<std::string> EPS_SET({"e"});

std::ostream &operator<<(std::ostream &stream, const std::set<std::string> &terminals);

class Grammar {
private:
    std::set<std::string> notTerminals;

    std::unordered_map<std::string, std::vector<std::vector<std::string>>> grammar;

    std::map <std::string, std::set<std::string>> FIRSTForG;

    std::map <std::string, std::set<std::string>> FOLLOWForG;

    std::string firstNonTerminal;

    bool initFIRSTWithTerminalsAndEpsilon();

    bool initFIRSTWithNonTerminals();

    bool initFOLLOW();

    bool calculateFOLLOW();


public:
    Grammar();

    ~Grammar();

    bool loadGrammar(std::ifstream stream);

    void printFIRST(std::ostream &stream);

    std::set<std::string> FIRST(const std::vector<std::string> &);

    std::set<std::string> FOLLOW(const std::string &);

    std::set<std::string> getNotTerminals() {
        return this->notTerminals;
    }

};

std::ostream &operator<<(std::ostream &stream, const Grammar &g);


#endif //HW11_GRAMMAR_H
