project(hw11)

set(HEADER_FILES grammar.h)
set(SOURCE_FILES grammar.cpp)

add_library(hw11 STATIC ${SOURCE_FILES} ${HEADER_FILES})