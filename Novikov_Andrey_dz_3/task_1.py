def num_translate(str_number):
    dict_numbers = {
        'один': 'one',
        'два': 'two',
        'три': 'three',
        'четыре': 'four',
        'пять': 'five',
        'шесть': 'six',
        'семь': 'seven',
        'восемь': 'eight',
        'девять': 'nine',
        'десять': 'ten',
    }
    return dict_numbers.get(str_number)


print(num_translate('один'))
print(num_translate('восемь'))
print(num_translate('двадцать'))
print(num_translate(''))
