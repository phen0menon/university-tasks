#include "gtest/gtest.h"
#include "hw3.h"

TEST(HomeWork3, TestToDecimal) {
    EXPECT_EQ(16, toDecimal("10000", 2));
    EXPECT_EQ(15, toDecimal("1111", 2));
    EXPECT_EQ(188, toDecimal("BC", 16));
    EXPECT_EQ(118, toDecimal("166", 8));
}

TEST(HomeWork3, TestFromDecimal) {
    EXPECT_EQ("1000000", fromDecimal(64, 2));
    EXPECT_EQ("111111", fromDecimal(63, 2));
    EXPECT_EQ("BC", fromDecimal(188, 16));
    EXPECT_EQ("422", fromDecimal(274, 8));
}


TEST(HomeWork3, TestStringSplit) {
    typedef std::vector<std::string> collection;

    {
        std::string example = "f g f";
        collection rightAns = { "f", "g", "f" };
        EXPECT_EQ(rightAns, split(example, ' '));
    }

    {
        std::string example = "dab";
        collection rightAns = { "d", "b" };
        EXPECT_EQ(rightAns, split(example, 'a'));
    }

    {
        std::string example = "a-b-c";
        collection rightAns = { "a", "b", "c" };
        EXPECT_EQ(rightAns, split(example, '-'));
    }
}

TEST(HomeWork3, TestSwapIntegers) {
    {
        int a = 3, b = 4;
        int tA = a, tB = b;
        swap(a, b);
        EXPECT_EQ(a, tB);
        EXPECT_EQ(b, tA);
    }
}

TEST(HomeWork3, TestBubbleSortUsingReferencableSwap) {
    typedef std::vector<int> collection;

    {
        collection example = {9, 8, 7, 6, 5};
        collection rightAns = {5, 6, 7, 8, 9};
        sortIntegers(example);
        EXPECT_EQ(example, rightAns);
    }

    {
        collection example = {100, 90, 1};
        collection rightAns = {1, 90, 100};
        sortIntegers(example);
        EXPECT_EQ(example, rightAns);
    }
}