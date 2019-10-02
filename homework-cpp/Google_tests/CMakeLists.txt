project(Google_tests)
add_subdirectory(lib)
include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})

# Tests
add_executable(Google_Tests_run hw3_test.cpp)

# Homeworks
target_link_libraries(Google_Tests_run hw3)

# Google Test Lib
target_link_libraries(Google_Tests_run gtest gtest_main)