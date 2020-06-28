#include <sstream>
#include "ps_automaton.h"

PSAutomatonCell::operator std::string() const {
    std::stringstream ss;
    bool useComma = false;
    switch (this->stackOperation) {
        case STACK_NOP:
            break;
        case REP:
            useComma = true;
            ss << "R" << this->stackOperationValue + 1;
            break;
        case POP:
            useComma = true;
            ss << "P";
            break;
    }
    switch (this->inputOperation) {
        case INPUT_NOP:
            break;
        case RET:
            if (useComma) ss << ',';
            ss << "R";
            useComma = true;
            break;
        case ADV:
            if (useComma) ss << ',';
            ss << "A";
            useComma = true;
            break;
    }
    switch (this->automatonCellReturn) {
        case CONTINUE:
            break;
        case ACCEPT:
            if (useComma) ss << ',';
            ss << "Accept";
            break;
        case REJECT:
            break;
    }
    return ss.str();
}

PSAutomatonCell::PSAutomatonCell(const PSAutomatonCellInputOperation inputOperation,
                                 const PSAutomatonCellStackOperation stackOperation,
                                 const PSAutomatonCellReturn psCellReturn, const int stackOperationValue)
        : inputOperation(inputOperation),
          stackOperation(stackOperation),
          automatonCellReturn(psCellReturn),
          stackOperationValue(
                  stackOperationValue) {}

bool PSAutomatonCell::operator<(const PSAutomatonCell &rhs) const {
    if (inputOperation < rhs.inputOperation)
        return true;
    if (rhs.inputOperation < inputOperation)
        return false;
    if (stackOperation < rhs.stackOperation)
        return true;
    if (rhs.stackOperation < stackOperation)
        return false;
    if (automatonCellReturn < rhs.automatonCellReturn)
        return true;
    if (rhs.automatonCellReturn < automatonCellReturn)
        return false;
    return stackOperationValue < rhs.stackOperationValue;
}

bool PSAutomatonCell::operator>(const PSAutomatonCell &rhs) const {
    return rhs < *this;
}

bool PSAutomatonCell::operator<=(const PSAutomatonCell &rhs) const {
    return !(rhs < *this);
}

bool PSAutomatonCell::operator>=(const PSAutomatonCell &rhs) const {
    return !(*this < rhs);
}

PSAutomatonCell::PSAutomatonCell() : stackOperationValue(0) {}

bool PSAutomatonCell::operator==(const PSAutomatonCell &rhs) const {
    return inputOperation == rhs.inputOperation &&
           stackOperation == rhs.stackOperation &&
           automatonCellReturn == rhs.automatonCellReturn &&
           stackOperationValue == rhs.stackOperationValue;
}

bool PSAutomatonCell::operator!=(const PSAutomatonCell &rhs) const {
    return !(rhs == *this);
}