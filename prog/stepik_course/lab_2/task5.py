from collections import Counter

def find_occurrencies():
    text = str(input())
    num_inputs = input().split(" ")

    k = int(num_inputs[0])
    L = int(num_inputs[1])
    t = int(num_inputs[2])

    curr_pos = 0
    occur = set()

    for curr_pos, i in enumerate(range(len(text) - L), 0):
        curr_str = text[curr_pos:L + curr_pos + 1]
        words = Counter(curr_str[i:i+k] for i in range(len(curr_str) - k + 1)).most_common()
        occur.update({word[0] for word in words if word[1] == t})

    print(" ".join(sorted(list(occur))))

if __name__ == "__main__":
	find_occurrencies()
