def convert_to_pattern(data, k):
    assoc_table = {"0": "A", "1": "C", "2": "G", "3": "T"}

    def number_to_pattern(number, pattern_length):
        converted_string = ""

        while number >= 4:
            converted_string += str(number % 4)
            number = number // 4

        converted_string += str(number)

        while len(converted_string) < pattern_length:
            converted_string += "0"

        return "".join(assoc_table[number] for number in reversed(converted_string))

    return number_to_pattern(data, k)

def convert_to_num(data):
    assoc_table = { "A": "0", "C": "1", "G": "2", "T": "3" }
    preconversed_data = [assoc_table[symbol] for symbol in data]

    return int("".join(preconversed_data), len(assoc_table))

def frequent_words_with_sorting(text, k):
    indices = sorted([convert_to_num(text[i : i + k]) for i in range(len(text) - k + 1)])
    count = [0] * len(indices)

    for i in range(len(indices)):
        count[i] += indices[:i + 1].count(indices[i])

    max_count = max(count)
    found_patterns = [indices[idx] for idx in range(len(indices)) if count[idx] == max_count]
    converted_indices = [convert_to_pattern(pattern, k) for pattern in found_patterns]

    print(*count)
    print(*converted_indices)

if __name__ == "__main__":
    frequent_words_with_sorting(input(), int(input()))