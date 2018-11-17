from math import log2 as logarithm

import io


class Parser(object):
    probabilities = []
    content = None

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

                    print_field = "\t{} {} {}".format(str(occurrence), str(probability), str(chance))

                    self.probabilities.append([(idx, float(probability)), [], None, ""])

                    print(idx.upper() + print_field)


    def sort_tree(self, vertex):
        return vertex[0][1]

    def huffman_encode(self, tree):
        if len(tree) <= 1:
            return tree

        tree.sort(key=self.sort_tree)

        left_son, right_son = tree[0], tree[1]
        left_son[3], right_son[3] = "0", "1"

        edge = [('', left_son[0][1] + right_son[0][1]), [left_son, right_son], None, ""]

        left_son[2], right_son[2] = edge, edge

        tree = tree[2:]
        tree.append(edge)

        return tree

    def get_huffman_tree_value(self, edge):
        code = edge[3]
        parent = edge[2]

        while parent is not None:
            code = parent[3] + code
            parent = parent[2]

        return code

    def get_huffman_encoding(self, tree):
        cl_tree = tree[:]

        while len(cl_tree) > 1:
            cl_tree = self.huffman_encode(cl_tree)

        return cl_tree

    def get_huffman_code_length(self):
        code_length = 0

        self.get_huffman_encoding(self.probabilities)

        for edge in self.probabilities:
            code_length += edge[0][1] * len(str(self.get_huffman_tree_value(edge)))

        return round(code_length, 7)

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
        print("\nLength of symbols is", self.get_symbols_count())
        print("Length of alphabet is", self.get_unique_symbols_count())
        print("Hartley entropy is", self.get_hartley_entropy())
        print("Hartley info amount is", self.get_hartley_inf_amount())
        print("Shannon entropy is", self.get_shannon_entropy())
        print("Shannon info amount is", self.get_shannon_inf_amount())
        print("Optimal Huffman's length of code is", self.get_huffman_code_length())


def main():
    path_to_file = "txt.txt"

    file_parser = Parser(path_to_file)
    file_parser.get_chars()
    file_parser.print_informatics_data()


if __name__ == '__main__':
    main()
