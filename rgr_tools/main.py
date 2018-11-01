from argparse import ArgumentParser
from os import listdir
from os.path import *

import io


class Parser(object):
    content = None

    def __init__(self, filename):
        try:
            with io.open(filename, 'r', encoding='utf8') as content_file:
                self.content = content_file.read().strip()
            
            self.alphabet = list(set(self.content))
        except FileNotFoundError:
            print("Файл не найден!")

            if len(str(filename).split('/')) <= 1:
                """
                Если файл ищется в локальной директории (директория, где запущен скрипт)
                """

                dir_path = dirname(abspath(__file__))
                print("Доступные файлы в текущей директории:\n", [f for f in listdir(dir_path) if isfile(join(dir_path, f))], sep='')

    def get_chars_dictionary(self):
        self.letters = dict()

        for letter in self.alphabet:
            self.letters[letter] = self.content.count(letter)

        self.dictionary = dict(sorted(self.letters.items(), key=lambda kv: kv[1], reverse=True))

    def get_chars(self):
        if self.content is not None:
            self.get_chars_dictionary()

            net_length = sum(self.dictionary.values())

            for idx in self.dictionary.keys():
                occurency = self.dictionary[idx]
                probability = '{:.7f}'.format(round(occurency / net_length, 7))
                chance = '{:.2f}%'.format((float(probability) * 100))

                if idx == ' ': print('пробел' + '%+8s' % str(occurency) + '%+18s' % str(probability) + '%+14s' % str(chance))
                elif idx != '\n': print(idx + '%+13s' % str(occurency) + '%+18s' % str(probability) + '%+14s' % str(chance))              


def main():
    argparser = ArgumentParser()
    argparser.add_argument("-f", "--file", dest="filename", help="Read some .txt-file and find repeat probability of each symbol")
    args = argparser.parse_args()

    file_parser = Parser(args.filename)
    file_parser.get_chars()

if __name__ == '__main__':
    main()