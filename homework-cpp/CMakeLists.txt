cmake_minimum_required(VERSION 3.14)
project(testing_test)

set(CMAKE_CXX_STANDARD 14)
set(SOURCE_FILES main.cpp)

add_executable(hw3_run ${SOURCE_FILES})

include_directories(hw3)
add_subdirectory(hw3)

target_link_libraries(hw3_run hw3)

add_subdirectory(Google_tests)


