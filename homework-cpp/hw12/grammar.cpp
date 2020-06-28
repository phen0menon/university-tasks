#include <iostream>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stack>
#include "grammar.h"
#include "utils.cpp"

Grammar::Grammar() = default;

Grammar::~Grammar() = default;

bool Grammar::loadGrammar(std::istream &stream) {
    std::string line;
    while (getline(stream, line)) {
        const std::vector<std::string> items = split(line, " -> ");

        const auto leftTerminal = items[0];
        const auto rightTerminals = split(items[1], " ");

        if (this->firstNonTerminal.empty()) {
            this->firstNonTerminal = leftTerminal;
        }

        if (grammar.find(leftTerminal) == grammar.end()) {
            grammar.insert({leftTerminal, std::vector<std::vector<std::string>>{rightTerminals}});
        } else {
            grammar.at(leftTerminal).push_back(rightTerminals);
        }

        this->enumeratedRules.emplace_back(leftTerminal, rightTerminals);
    }

    auto it = grammar.begin();
    while (it != grammar.end()) {
        for (const auto &s : it->second) {
            for (const auto &_s : s) {
                if (grammar.find(_s) != grammar.end() && _s != "e") {
                    notTerminals.insert(_s);
                } else {
                    terminals.insert(_s);
                }
            }
        }
        it++;
    }

    if (!initFIRSTWithTerminalsAndEpsilon()) return false;
    if (!initFIRSTWithNonTerminals()) return false;

    return calculateFOLLOW();
}

std::ostream &operator<<(std::ostream &stream, const Grammar &g) {
    // Вставляем код задачи 5.1.1
    return stream;
}

bool Grammar::initFIRSTWithTerminalsAndEpsilon() {
    for (const auto &_g : grammar) {
        FIRSTForG.insert({_g.first, std::set<std::string>()});
        for (const auto &r : _g.second) {
            for (const auto &x : r) {
                if (notTerminals.find(x) == notTerminals.end()) {
                    FIRSTForG.insert({x, std::set<std::string>{x}});
                }

                if (x == EPSILON) {
                    const auto el = FIRSTForG.find(_g.first);
                    if (el != FIRSTForG.end()) {
                        el->second.insert({x});
                    }
                }
            }
        }
    }

    return true;
}

void Grammar::printFIRST(std::ostream &stream) {
    for (auto &pair : FIRSTForG) {
        if (pair.second.empty()) continue;
        stream << pair.first << " = " << pair.second;
    }
}

void Grammar::printFOLLOW(std::ostream &stream) {
    for (const auto &pair : FOLLOWForG) {
        const std::string &leftPart = pair.first;
        const std::set<std::string> &rightPart = pair.second;
        stream << leftPart << " = " << rightPart;
    }
}

std::set<std::string> Grammar::FIRST(const std::vector<std::string> &str) {
    std::set<std::string> result;

    if (str.size() == 1) {
        if (str[0] == "e") {
            result.insert(str[0]);
        } else {
            const auto ffG = FIRSTForG.find(str[0]);
            if (ffG != FIRSTForG.end()) {
                result = ffG->second;
            }
        }
    } else {
        auto index = 0;
        for (const auto &t : str) {
            std::set<std::string> tempRes = FIRST(std::vector<std::string>{t});

            for (const auto &_t : tempRes) {
                if (_t != "e") {
                    result.insert({_t});
                }
            }

            if (!contains(tempRes, "e")) {
                break;
            }

            if (++index == str.size()) {
                result.insert({"e"});
            }
        }
    }

    return result;
}

bool Grammar::initFIRSTWithNonTerminals() {
    for (const auto &g : grammar) {
        bool hasNewMember = false;
        for (auto &rule : g.second) {
            for (const std::string &_first : FIRST(rule)) {
                hasNewMember = !contains(FIRSTForG[g.first], _first);
                FIRSTForG[g.first].insert(_first);
            }
            if (!hasNewMember) {
                break;
            }
        }
    }

    return true;
}

bool Grammar::initFOLLOW() {
    for (auto[it, index] = std::make_tuple(grammar.begin(), 0); it != grammar.end(); ++it, ++index) {
        FOLLOWForG.insert({it->first, std::set<std::string>()});

        if (index == 0) {
            FOLLOWForG.insert({this->firstNonTerminal, std::set<std::string>{"$"}});
        }
    }

    return true;
}

std::ostream &operator<<(std::ostream &stream, const std::set<std::string> &terminals) {
    auto p = terminals.begin();
    stream << "[";
    while (p != terminals.end()) {
        stream << p->c_str();
        p++;
        if (p != terminals.end()) stream << " ";
    }
    stream << "]" << std::endl;

    return stream;
}

bool Grammar::calculateFOLLOW() {
    initFOLLOW();

    bool changed = true;
    while (changed) {
        changed = false;
        for (auto const&[nonTerm, rules] : grammar) {
            for (auto const &rule : rules) {
                std::unordered_map<int, std::string> enumerated;
                for (size_t i = 0; i < rule.size(); ++i) {
                    if (contains(this->notTerminals, rule.at(i))) {
                        enumerated.insert(std::make_pair(i, rule.at(i)));
                    }
                }

                for (auto const&[index, nonTerminal] : enumerated) {
                    std::vector<std::string> beta(rule.begin() + index + 1, rule.end());
                    std::set<std::string> _first = FIRST(beta);
                    std::set<std::string> diff = calculateDiff(_first, EPS_SET);
                    if (hasDiff(diff, FOLLOWForG.at(nonTerminal))) {
                        changed = true;
                    }
                    FOLLOWForG.at(nonTerminal).insert(diff.begin(), diff.end());
                    if ((beta.empty()) || (contains(_first, "e"))) {
                        std::set<std::string> _newFirst = FOLLOWForG.at(nonTerm);
                        if (hasDiff(_newFirst, FOLLOWForG.at(nonTerminal))) {
                            changed = true;
                        }
                        FOLLOWForG.at(nonTerminal).insert(_newFirst.begin(), _newFirst.end());
                    }
                }
            }
        }
    }

    return true;
}

std::set<std::string> Grammar::FOLLOW(const std::string &word) {
    if (!isNonTerminal(word)) {
        return std::set<std::string>();
    }
    return FOLLOWForG[word];
}

bool Grammar::isTerminal(const std::string &word) {
    if (word == EPSILON) return false;
    return contains(terminals, word);
}

bool Grammar::isNonTerminal(const std::string &word) {
    if (word == EPSILON) return false;
    return contains(notTerminals, word);
}

// HW 12
void Grammar::printSATable() {
    // too long to implement ..
}

bool Grammar::buildSATable() {
    if (!saTable.empty()) {
        saTable.clear();
    }
    for (const std::string &word : combine(combine(notTerminals, terminals), std::set<std::string>{"$"})) {
        for (const std::string &term : combine(terminals, std::set<std::string>{"$"})) {
            saTable.emplace(word, std::map<std::string, std::set<PSAutomatonCell>>());
            saTable[word].emplace(term, std::set<PSAutomatonCell>());
        }
    }

    for (int i = 0; i < enumeratedRules.size(); ++i) {
        const auto &pair = enumeratedRules[i];
        const std::string &leftPart = pair.first;
        const std::vector<std::string> rightPart = pair.second;
        const std::set<std::string> rightPartFirst = FIRST(rightPart);
        const std::set<std::string> firstTerminals = filter(rightPartFirst, [this](const std::string &w) {
            return isTerminal(w);
        });
        for (const std::string &terminal : firstTerminals) {
            saTable[leftPart][terminal].emplace(
                    PSAutomatonCell(
                            PSAutomatonCellInputOperation::RET,
                            PSAutomatonCellStackOperation::REP,
                            PSAutomatonCellReturn::CONTINUE,
                            i)
            );
        }
        if (contains(rightPartFirst, EPSILON)) {
            for (const std::string &term : FOLLOW(leftPart)) {
                saTable[leftPart][term].emplace(
                        PSAutomatonCell(
                                PSAutomatonCellInputOperation::RET,
                                PSAutomatonCellStackOperation::REP,
                                PSAutomatonCellReturn::CONTINUE,
                                i)
                );
            }
        }
    }
    for (const std::string &term : terminals) {
        saTable[term][term].emplace(
                PSAutomatonCell(
                        PSAutomatonCellInputOperation::ADV,
                        PSAutomatonCellStackOperation::POP,
                        PSAutomatonCellReturn::CONTINUE,
                        0)
        );
    }
    saTable["$"]["$"].emplace(
            PSAutomatonCell(
                    PSAutomatonCellInputOperation::INPUT_NOP,
                    PSAutomatonCellStackOperation::STACK_NOP,
                    PSAutomatonCellReturn::ACCEPT,
                    0)
    );
    bool isLL1 = true;
    for (auto &pair1 : saTable) {
        for (auto &pair2 : pair1.second) {
            if (pair2.second.size() >= 2) {
                isLL1 = false;
            }
        }
    }
    return isLL1;
}


bool Grammar::parse(std::istream &stream) {
    std::stack<std::string> stack;
    stack.push("$");
    stack.push(firstNonTerminal);
    std::string currTerminal;
    bool requireNextSymbol = true;
    PSAutomatonCell psAutomatonCell;
    while (true) {
        if (requireNextSymbol) {
            if (stream.eof()) {
                currTerminal = "";
            } else {
                stream >> currTerminal;
            }
            requireNextSymbol = false;
        }
        const std::string &currInputTerminal = currTerminal.empty() ? "$" : currTerminal;
        std::set<PSAutomatonCell> set = saTable[stack.top()][currInputTerminal];
        if (set.size() >= 2) {
//            return false;
        } else if (set.size() == 1) {
            psAutomatonCell = *set.begin();
        } else {
            psAutomatonCell = PSAutomatonCell();
        }
        int ruleNumber;
        std::vector<std::string> *rightSide;
        switch (psAutomatonCell.stackOperation) {
            case STACK_NOP:
                break;
            case REP:
                if (stack.top() != "$") stack.pop();
                ruleNumber = psAutomatonCell.stackOperationValue;
                rightSide = &enumeratedRules[ruleNumber].second;
                if (*rightSide != std::vector<std::string>{EPSILON}) {
                    for (auto it = rightSide->rbegin(); it != rightSide->rend(); it++) {
                        stack.push(*it);
                    }
                }
                break;
            case POP:
                stack.pop();
                break;
        }
        switch (psAutomatonCell.inputOperation) {
            case INPUT_NOP:
            case RET:
                break;
            case ADV:
                requireNextSymbol = true;
                break;
        }
        switch (psAutomatonCell.automatonCellReturn) {
            case CONTINUE:
                break;
            case ACCEPT:
                return true;
            case REJECT:
                return false;
        }
    }
}

