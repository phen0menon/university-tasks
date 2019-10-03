project(hw3)

set(HEADER_FILES hw3.h)
set(SOURCE_FILES hw3.cpp)

add_library(hw3 STATIC ${SOURCE_FILES} ${HEADER_FILES})