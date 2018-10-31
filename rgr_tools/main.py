from argparse import ArgumentParser
from os import listdir
from os.path import *

import io


class File(object):
    content = None

    def __init__(self, filename):
        try:
            with io.open(filename, 'r', encoding='utf8') as content_file:
                self.content = content_file.read()
            
            self.ALPHABET = [chr(i) for i in range(ord('а'), ord('я') + 1)]
            self.ALPHABET.extend([' ', ',', '-', '_', '?', '"', ':', '!', ';'])
            self.ALPHABET.extend(str(i) for i in range(0, 10))
        except FileNotFoundError:
            print("Файл не найден!")

            if len(str(filename).split('/')) <= 1:
                """
                Если файл ищется в локальной директории (директория, где запущен скрипт)
                """
                
                dir_path = dirname(abspath(__file__))
                print("Доступные файлы в текущей директории:\n", [f for f in listdir(dir_path) if isfile(join(dir_path, f))])

    def get_chars_dictionary(self):
        self.letters = dict()

        for letter in self.ALPHABET:
            self.letters[letter] = self.content.count(letter)

        self.dictionary = dict(sorted(self.letters.items(), key=lambda kv: kv[1], reverse=True))

    def get_chars(self):
        if self.content is not None:
            self.get_chars_dictionary()

            net_length = sum(self.dictionary.values())
            
            print("Символ   Повторения    Вероятность")
            for idx in self.dictionary.keys():
                current_symbol = self.dictionary[idx]
                probability = '{:.7f}'.format(round(current_symbol / net_length, 7))

                if idx == ' ':
                    print('пробел' + '%+8s' % str(current_symbol) + '%+18s' % str(probability))
                else: print(idx + '%+13s' % str(current_symbol) + '%+18s' % str(probability))              


def main():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", help="Read some .txt-file and find repeat probability of each symbol")
    args = parser.parse_args()

    file = File(args.filename)
    file.get_chars()

if __name__ == '__main__':
    main()