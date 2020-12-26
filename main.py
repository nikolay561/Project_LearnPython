import random

topics = ['погода', 'напоминание']

def guess_topic(text):
	if text == text:
		result = topics[random.randint(0, 1)]
		return result

text = input('Введите текст: ')
result = guess_topic(text)
print(result)