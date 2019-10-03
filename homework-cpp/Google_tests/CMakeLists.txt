project(Google_tests)
add_subdirectory(lib)
include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})

# Tests
add_executable(Google_Tests_hw3 hw3_test.cpp)
add_executable(Google_Tests_hw2 hw2_test.cpp)

# Homeworks
target_link_libraries(Google_Tests_hw3 hw3)
target_link_libraries(Google_Tests_hw2 hw2)

# Google Test Lib
target_link_libraries(Google_Tests_hw3 gtest gtest_main)
target_link_libraries(Google_Tests_hw2 gtest gtest_main)