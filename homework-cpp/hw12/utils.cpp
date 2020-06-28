#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

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

std::set<std::string> calculateIntersection(const std::set<std::string> &a, std::set<std::string> &b) {
    std::set<std::string> inter;
    std::set_intersection(a.begin(), a.end(), b.begin(), b.end(), std::inserter(inter, inter.begin()));
    return inter;
}

std::set<std::string> combine(const std::set<std::string> &set1, const std::set<std::string> &set2) {
    std::set<std::string> out;
    std::set_union(set1.begin(), set1.end(), set2.begin(), set2.end(), std::inserter(out, out.begin()));
    return out;
}

std::vector<std::string> combine(const std::vector<std::string> &vector1, const std::vector<std::string> &vector2) {
    std::vector<std::string> out;
    out.insert(out.begin(), vector1.begin(), vector1.end());
    out.insert(out.end(), vector2.begin(), vector2.end());
    return out;
}


std::vector<std::string>
filter(const std::vector<std::string> &str, const std::function<bool(std::string)> &predicate) {
    std::vector<std::string> result(str.size());
    for (const std::string &word: str) {
        if (predicate(word)) {
            result.push_back(word);
        }
    }
    return result;
}

std::set<std::string> filter(const std::set<std::string> &str, const std::function<bool(std::string)> &predicate) {
    std::set<std::string> result;
    for (const std::string &word: str) {
        if (predicate(word)) {
            result.insert(word);
        }
    }
    return result;
}

bool hasDiff(const std::set<std::string> &a, const std::set<std::string> &b) {
    return !calculateDiff(a, b).empty();
}

std::string fromVectorReversed(std::vector<std::string> v) {
    std::string s;
    for (auto i = v.rbegin(); i != v.rend(); ++i) {
        s += *i;
    }
    return s;
}

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
