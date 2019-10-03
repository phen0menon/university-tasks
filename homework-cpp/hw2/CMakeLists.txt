project(hw2)

set(HEADER_FILES hw2.h)
set(SOURCE_FILES hw2.cpp)

add_library(hw2 STATIC ${SOURCE_FILES} ${HEADER_FILES})