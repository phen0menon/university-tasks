cmake_minimum_required(VERSION 3.14)
project(homework)

set(CMAKE_CXX_STANDARD 14)
set(SOURCE_FILES main.cpp)

# Connect directories
include_directories(hw4 hw3 hw2)
add_subdirectory(hw4)
add_subdirectory(hw3)
add_subdirectory(hw2)

# Run pointers
add_executable(hw4_run ${SOURCE_FILES})
add_executable(hw3_run ${SOURCE_FILES})
add_executable(hw2_run ${SOURCE_FILES})

# Target libs
target_link_libraries(hw4_run hw4)
target_link_libraries(hw3_run hw3)
target_link_libraries(hw2_run hw2)

add_subdirectory(Google_tests)


