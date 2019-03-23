"""
Реализуйте алгоритм FasterFrequentWords, который находит в строке наиболее частую подстроку заданного размера, используя массив частот. Ответ выдайте в лексикографическом порядке.

Вход: Строка Text и число k.
Выход: Все наиболее частые подстроки длины k из строки Text, отсортированные по алфавиту.


Sample Input:
ACGTTGCATGTCGCATGATGCATGAGAGCT
4

Sample Output:
CATG GCAT
"""

# import timeit
from collections import Counter

def find_occurrencies():
	text = input()
	k = int(input())

	words = Counter(text[i:i+k] for i in range(len(text) - k + 1)).most_common()
	print(" ".join(sorted([word[0] for word in words if word[1] == words[0][1]])))

if __name__ == "__main__":
	find_occurrencies()
	# print(timeit.timeit(find_occurrencies, number=10))
	# 5.9 - 6.05 avg time for 10 func calls
