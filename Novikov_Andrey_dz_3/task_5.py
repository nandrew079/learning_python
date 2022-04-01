from random import choice


def get_jokes(number_jokes):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_jokes = []

    for i in range(number_jokes):
        list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return list_jokes


print(get_jokes(2))
