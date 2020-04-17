#include "grammar.cpp"

int main() {
    Grammar G = Grammar();
    G.loadGrammar(std::ifstream("C:\\Development\\university-tasks\\homework-cpp\\hw11\\grammar.txt"));

    for (const auto& nonTerminal : G.getNotTerminals()) {
        std::cout << nonTerminal << " " << G.FOLLOW(nonTerminal);
    }

    return 0;
}