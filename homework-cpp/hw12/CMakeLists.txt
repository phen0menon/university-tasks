project(hw12)

set(HEADER_FILES grammar.h ps_automaton.cpp ps_automaton.h)
set(SOURCE_FILES grammar.cpp ps_automaton.cpp ps_automaton.h utils.cpp)

add_library(hw12 STATIC ${SOURCE_FILES} ${HEADER_FILES})