def convert(substr):
    assoc_table = {"A": "0", "C": "1", "G": "2", "T": "3"}
    return int("".join([assoc_table[string] for string in list(substr)]), 4)

if __name__ == "__main__":
    text = str(input())
    k = int(input())

    acid_dna = [0] * (4 ** k)

    for i in range(len(text) - k + 1):
        acid_dna[convert(text[i:i+k])] = acid_dna[convert(text[i:i+k])] + 1

    print(*acid_dna, sep=' ')
