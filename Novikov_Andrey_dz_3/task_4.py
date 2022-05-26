import pprint


def thesaurus_adv(*args):
    new_dict = {}
    for item in args:
        str_item = str(item)
        list_item = str_item.split()

        first_symbol_name = list_item[0][0]
        first_symbol_surname = list_item[1][0]

        if new_dict.get(first_symbol_surname) is None:
            new_dict[first_symbol_surname] = {}

        if new_dict[first_symbol_surname].get(first_symbol_name) is None:
            new_dict[first_symbol_surname][first_symbol_name] = []

        new_dict[first_symbol_surname][first_symbol_name].append(item)

    return new_dict


pprint.pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"), sort_dicts=False)

# Как поступить, если потребуется сортировка по ключам?
# dict_names = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# sorted_tuple = sorted(dict_names.items(), key=lambda x: x[0])
# print('\n')
# pprint.pprint(dict(sorted_tuple), sort_dicts=False)
