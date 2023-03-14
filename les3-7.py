def int_func(word):
    return word.title()

words = input('Введите слова через пробел: ')
words_list = words.split()

result = []
for word in words_list:
    result.append(int_func(word))

print(' '.join(result))