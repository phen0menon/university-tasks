#include <iostream>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include "grammar.h"

template<typename T, typename Iterator>
bool contains(Iterator it1, Iterator it2, const T &value) {
    return std::find(it1, it2, value) != it2;
}

template<typename T, typename Container>
bool contains(const Container &c, const T &value) {
    return contains(c.begin(), c.end(), value);
}

std::set<std::string> calculateDiff(const std::set<std::string> &a, const std::set<std::string> &b) {
    std::set<std::string> diff;
    std::set_difference(a.begin(), a.end(), b.begin(),
                        b.end(),
                        std::inserter(diff, diff.begin()));
    return diff;
}

bool hasDiff(const std::set<std::string> &a, const std::set<std::string> &b) {
    return !calculateDiff(a, b).empty();
}

Grammar::Grammar() = default;

Grammar::~Grammar() = default;

std::vector<std::string> split(std::string s, const std::string &delimiter) {
    size_t pos = 0;
    std::string token;
    std::vector<std::string> items;
    while ((pos = s.find(delimiter)) != std::string::npos) {
        token = s.substr(0, pos);
        items.push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    items.push_back(s);
    return items;
}


bool Grammar::loadGrammar(std::ifstream stream) {
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
    }

    auto it = grammar.begin();
    while (it != grammar.end()) {
        for (const auto &s : it->second) {
            for (const auto &_s : s) {
                if (grammar.find(_s) != grammar.end() && _s != "e") {
                    notTerminals.insert(_s);
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

                if (x == "e") {
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
    auto it = FIRSTForG.begin();
    while (it != FIRSTForG.end()) {
        auto key = it->first;
        auto strings = it->second;

        for (const auto &s: strings) {
            stream << key << " = [" << s << "]" << "\n";
        }
        it++;
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

std::set<std::string> Grammar::FOLLOW(const std::string &N) {
    return FOLLOWForG[N];
}

