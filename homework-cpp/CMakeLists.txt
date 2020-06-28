cmake_minimum_required(VERSION 3.14)
project(homework)

set(CMAKE_CXX_STANDARD 17)
set(SOURCE_FILES main.cpp)

# Connect directories
include_directories(hw4 hw12)
add_subdirectory(hw4)
add_subdirectory(hw12)

# Run pointers
add_executable(hw4_run ${SOURCE_FILES})
add_executable(hw12_run ${SOURCE_FILES})

# Target libs
target_link_libraries(hw4_run hw4)
target_link_libraries(hw12_run hw12)

add_subdirectory(Google_tests)
add_subdirectory(Catch_tests)
