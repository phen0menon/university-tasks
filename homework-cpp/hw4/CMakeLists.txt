project(hw4)

set(HEADER_FILES hw4.h token.hpp scanner.hpp)
set(SOURCE_FILES hw4.cpp token.cpp scanner.cpp)

add_library(hw4 STATIC ${SOURCE_FILES} ${HEADER_FILES})