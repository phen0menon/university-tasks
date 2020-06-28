#ifndef HOMEWORK_PS_AUTOMATON_H
#define HOMEWORK_PS_AUTOMATON_H


#include <string>

enum PSAutomatonCellStackOperation {
    STACK_NOP, REP, POP
};

enum PSAutomatonCellInputOperation {
    INPUT_NOP, RET, ADV
};

enum PSAutomatonCellReturn {
    CONTINUE, ACCEPT, REJECT
};

class PSAutomatonCell {
public:
    PSAutomatonCellInputOperation inputOperation = INPUT_NOP;
    PSAutomatonCellStackOperation stackOperation = STACK_NOP;
    PSAutomatonCellReturn automatonCellReturn = REJECT;
    int stackOperationValue;

    PSAutomatonCell();

    PSAutomatonCell(PSAutomatonCellInputOperation inputOperation, PSAutomatonCellStackOperation stackOperation,
                    PSAutomatonCellReturn psCellReturn, int stackOperationValue);

    explicit operator std::string() const;

    bool operator<(const PSAutomatonCell &rhs) const;

    bool operator>(const PSAutomatonCell &rhs) const;

    bool operator<=(const PSAutomatonCell &rhs) const;

    bool operator==(const PSAutomatonCell &rhs) const;

    bool operator!=(const PSAutomatonCell &rhs) const;

    bool operator>=(const PSAutomatonCell &rhs) const;
};


#endif //HOMEWORK_PS_AUTOMATON_H
