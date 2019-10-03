#include "gtest/gtest.h"
#include "hw2.h"

TEST(HomeWork2, isMinimumFindingCorrect) {
    typedef std::vector<float> collection;

    {
        collection test = {9.8, 10.5, 1.5};
        ASSERT_EQ(2, getIndexOfMinimum(test));
    }

    {
        collection test = {1.0, -1.5, 2.0};
        ASSERT_EQ(1, getIndexOfMinimum(test));
    }
}

TEST(HomeWork2, isRangeCreationCorrect) {
    typedef std::vector<int> collection;

    {
        collection test = {1,13,50};
        ASSERT_EQ(test, range(3));
    }

    {
        collection test = {1, 13, 50, 126};
        ASSERT_EQ(test, range(4));
    }
}

TEST(HomeWork2, testIsPalyndrome) {
    typedef std::vector<int> collection;

    {
        collection test = {1,2,3,3,2,1};
        ASSERT_EQ(true, isPalyndrome(test));
    }

    {
        collection test = {5,5,5,4,4,4};
        ASSERT_EQ(false, isPalyndrome(test));
    }
}