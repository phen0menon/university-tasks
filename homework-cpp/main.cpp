#include "grammar.h"

int main() {
    Grammar G = Grammar();
    std::ifstream stream("./grammar.txt");
    G.loadGrammar(stream);
    G.buildSATable();
    return 0;
}