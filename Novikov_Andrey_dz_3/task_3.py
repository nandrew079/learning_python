def thesaurus(*args):
    new_dict = {}
    for item in args:
        str_item = str(item)
        first_symbol = str_item[0]
        if new_dict.get(first_symbol) is None:
            new_dict[first_symbol] = []
        new_dict[first_symbol].append(item)

    return new_dict


print(thesaurus("Иван", "Петр", "Илья", "Мария"))

# Как поступить, если потребуется сортировка по ключам?
# dict_names = thesaurus("Иван", "Петр", "Илья", "Мария")
# sorted_tuple = sorted(dict_names.items(), key=lambda x: x[0])
# print(dict(sorted_tuple))
