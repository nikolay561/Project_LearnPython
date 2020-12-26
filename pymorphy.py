import pymorphy2

user_word = input('Введите слово: ')
morph = pymorphy2.MorphAnalyzer()
normal = morph.parse(user_word)[0].normal_form
print(normal)