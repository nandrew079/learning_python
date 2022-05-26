def get_elem(i, list_elem):
    if i >= len(list_elem):
        return None
    else:
        return list_elem[i]


def tuple_gen(list_1, list_2):
    return ((list_1[i], get_elem(i, list_2))
            for i in range(len(list_1)))


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

gen_tuple = tuple_gen(tutors, klasses)
print(type(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
