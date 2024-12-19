class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = tuple(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    words.extend(line.lower().translate(line.maketrans('', '', ',.=!?;:')).replace(' - ', ' ').split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        low_word = word.lower()
        found_words = {}
        for file_name, words in self.get_all_words().items():
            for i in range(len(words)):
                if low_word == words[i]:
                    found_words[file_name] = i + 1
                    break
        return found_words

    def count(self, word):
        low_word = word.lower()
        count_words = {}
        for file_name, words in self.get_all_words().items():
            count = 0
            for word_i in words:
                if low_word == word_i:
                    count += 1
            count_words[file_name] = count
        return count_words


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

#test All
    # finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
    #                       'Rudyard Kipling - If.txt',
    #                       'Mother Goose - Monday’s Child.txt')
    # print(finder1.get_all_words())
    # print(finder1.find('the'))
    # print(finder1.count('the'))

#test Mother Goose - Monday’s Child.txt
    # finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
    # print(finder1.get_all_words())
    # print(finder1.find('Child'))
    # print(finder1.count('Child'))

#test Rudyard Kipling - If.txt
    # finder1 = WordsFinder('Rudyard Kipling - If.txt', )
    # print(finder1.get_all_words())
    # print(finder1.find('if'))
    # print(finder1.count('if'))

#test Walt Whitman - O Captain! My Captain!.txt
    # finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    # print(finder1.get_all_words())
    # print(finder1.find('captain'))
    # print(finder1.count('captain'))
