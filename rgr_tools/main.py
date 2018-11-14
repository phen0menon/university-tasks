from argparse import ArgumentParser
from os import listdir
from os.path import *

import io


class Parser(object):
    content = None

    def __init__(self, filename):
        with io.open(filename, 'r', encoding='utf8') as content_file:
            self.content = content_file.read().strip().lower()
        
        self.alphabet = list(set(self.content))

    def get_chars_dictionary(self):
        self.letters = dict()
        self.letters = {letter: self.content.count(letter) for letter in self.alphabet}

        self.dictionary = dict(sorted(self.letters.items(), key=lambda kv: kv[1], reverse=True))

    def get_chars(self):
        if self.content is not None:
            self.get_chars_dictionary()

            net_length = sum(self.dictionary.values())

            for idx in self.dictionary.keys():
                occurency = self.dictionary[idx]
                probability = '{:.7f}'.format(round(occurency / net_length, 7))
                chance = '{:.2f}%'.format((float(probability) * 100))

                if idx == ' ': 
                    print('пробел'.upper() + '%+8s' % str(occurency) + '%+18s' % str(probability) + '%+14s' % str(chance))
                elif idx != '\n': 
                    print(idx.upper() + '%+13s' % str(occurency) + '%+18s' % str(probability) + '%+14s' % str(chance))              


def main():
    path_to_file = "txt.txt"

    file_parser = Parser(path_to_file)
    file_parser.get_chars()

if __name__ == '__main__':
    main()