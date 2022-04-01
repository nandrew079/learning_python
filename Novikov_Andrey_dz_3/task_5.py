from random import choice


def get_jokes(number_jokes, repeat_words=True):
    """
    Returm list jokes
    :param number_jokes:
    :param repeat_words:
    :return: list
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_jokes = []
    used_none = []
    used_adverb = []
    used_adjective = []

    for i in range(number_jokes):
        if not repeat_words:
            noun = get_unique_word(nouns, used_none)
            adverb = get_unique_word(adverbs, used_adverb)
            adjective = get_unique_word(adjectives, used_adjective)
        else:
            noun = choice(nouns)
            adverb = choice(adverbs)
            adjective = choice(adjectives)

        if not(noun and adverb and adjective):
            break

        list_jokes.append(f'{noun} {adverb} {adjective}')

    return list_jokes


def get_unique_word(list_words, used_list):
    """
    Returns an unused word from the list or an empty string if not found
    :param list_words:
    :param used_list:
    :return: str
    """
    word = ''
    if len(list_words) != len(used_list):
        word = choice(list_words)
        while used_list.count(word) != 0:
            word = choice(list_words)
        used_list.append(word)

    return word


print(get_jokes(7))
print(get_jokes(7, repeat_words=False))
