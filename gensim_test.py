import gensim
from gensim import corpora
from gensim import models
import numpy as np
from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count
import gensim.downloader as api

user_text = ['привет, как твои дела',
			'как поживаешь',
			'как жизнь',
			'как дела, как поживаешь']

# Создание словаря
texts = [[text for text in doc.split()] for doc in user_text]
dictionary = corpora.Dictionary(texts)

# Создание корпуса (мешка) слов
corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in texts]
print(dictionary)
print(corpus)

#  Проверка на повторение слов
word_counts = [[(dictionary[id], count) for id, count in line] for line in corpus]
print(word_counts)

# Информация о весомости слова
for doc in corpus:
	print([[dictionary[id], freq] for id, freq in doc])

# Создание модели веса слова TF-IDF
tfidf = models.TfidfModel(corpus, smartirs='ntc')

# Показ модели веса слова TF-IDF
for doc in tfidf[corpus]:
	print([[dictionary
		[id], np.around(freq, decimals=2)] for id, freq in doc])

# Создание биграммы так работает
# dataset = api.load('text8')
# dataset = [wd for wd in dataset]
# dct = corpora.Dictionary(dataset)
# corp = [dct.doc2bow(line) for line in dataset]
# bigram = gensim.models.phrases.Phrases(dataset, min_count=3, threshold=10)
# print(bigram[dataset[0]])

# А вот так почему-то нет, только буквы выводит. Вопрос: Я так понимаю необязательно создавать словарь и корпус для создания биграмммы?
dataset = user_text
dataset = [wd for wd in dataset]
# dct = corpora.Dictionary(dataset) 
# corp = [dct.doc2bow(line) for line in dataset]
bigram = gensim.models.phrases.Phrases(dataset, min_count=3, threshold=10)
print(bigram[dataset[0]])

# Создание триграммы


# Создание тематической модели
# не ставится пакет pattern, лог в папке проекта

# Модель Word2Vec
# dataset = api.load('text8')
# data = [d for d in dataset]
# data_part1 = data[:1000]
# data_part2 = data[1000:]
# model = Word2Vec(data_part1, min_count=0, workers=cpu_count())
# model['topic']
# test = model.most_similar('topic')
# print(test)

# Word2Vec user_text не работает на моем тексте, наверно в user_text надо данные как-то по другому записывать или по другому извлекать,
# не пойму как открыть text8, что бы посмотреть как там это выглядит, при команде print(dataset), пишет <text8.Dataset object at 0x20FBED48>
dataset = user_text
data = [d for d in dataset]
data_part1 = data[:1000]
model = Word2Vec(data_part1, min_count=0, workers=cpu_count())
model['topic']
test = model.most_similar('topic')
print(test)
