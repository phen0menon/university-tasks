from math import log2 as logarithm

import io


class Parser(object):
    content = None
    csv_output = []

    def __init__(self, filename):
        with io.open(filename, 'r', encoding='utf8') as content_file:
            self.content = content_file.read().strip().lower()

        self.alphabet = list(set(self.content))
        self.letters = {letter: self.content.count(letter) for letter in self.alphabet}
        self.dictionary = dict(sorted(self.letters.items(), key=lambda kv: kv[1], reverse=True))

    def get_chars(self):
        if self.content:
            net_length = sum(self.dictionary.values())

            for idx in self.dictionary.keys():
                if idx != '\n':
                    occurrence = self.dictionary[idx]

                    probability = '{:.7f}'.format(round(occurrence / net_length, 7))
                    chance = '{:.2f}%'.format((float(probability) * 100))

                    print_field = " {} {} {}".format(str(occurrence), str(probability), str(chance))

                    print(idx.upper() + print_field)

    def get_symbols_count(self):
        return len(self.content)

    def get_unique_symbols_count(self):
        return len(self.alphabet)

    def get_hartley_entropy(self):
        return logarithm(self.get_unique_symbols_count())

    def get_hartley_inf_amount(self):
        return self.get_hartley_entropy() * self.get_symbols_count()

    def get_shannon_entropy(self):
        entropy = 0

        for letter in self.dictionary.keys():
            letter_occurrence = self.dictionary[letter]

            entropy += letter_occurrence / self.get_symbols_count() * logarithm(
                1 / (letter_occurrence / self.get_symbols_count()))

        return entropy

    def get_shannon_inf_amount(self):
        return self.get_shannon_entropy() * self.get_symbols_count()

    def print_informatics_data(self):
        print("Length of symbols is", self.get_symbols_count())
        print("Length of alphabet is", self.get_unique_symbols_count())
        print("Hartley entropy is", self.get_hartley_entropy())
        print("Hartley info amount is", self.get_hartley_inf_amount())
        print("Shannon entropy is", self.get_shannon_entropy())
        print("Shannon info amount is", self.get_shannon_inf_amount())


def main():
    import time
    start_time = time.time()
    path_to_file = "txt.txt"

    file_parser = Parser(path_to_file)
    file_parser.get_chars()
    file_parser.print_informatics_data()
    elapsed_time = time.time() - start_time

    print(elapsed_time)


if __name__ == '__main__':
    main()
