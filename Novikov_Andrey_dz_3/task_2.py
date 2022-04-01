def num_translate_adv(str_number):
    dict_numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    result = None

    if str_number.istitle():
        result = dict_numbers.get(str_number.lower())
        if not(result is None):
            result = result.title()
    else:
        result = dict_numbers.get(str_number.lower())

    return result


print(num_translate_adv('one'))
print(num_translate_adv('Eight'))
print(num_translate_adv('twenty'))
print(num_translate_adv(''))
