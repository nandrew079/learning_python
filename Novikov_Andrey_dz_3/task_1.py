def num_translate(str_number):
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
    return dict_numbers.get(str_number)


print(num_translate('one'))
print(num_translate('eight'))
print(num_translate('twenty'))
print(num_translate(''))
