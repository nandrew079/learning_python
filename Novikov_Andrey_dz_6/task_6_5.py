import sys


def get_elem(ind, list_elem):
    elem = None
    if ind < len(list_elem):
        elem = list_elem[ind]
    return elem


if __name__ == '__main__':

    if get_elem(1, sys.argv) is None:
        user_file = 'users.csv'
    else:
        user_file = sys.argv[1]

    if get_elem(2, sys.argv) is None:
        hobby_file = 'hobby.csv'
    else:
        hobby_file = sys.argv[2]

    if get_elem(3, sys.argv) is None:
        result_file = 'user_hobby.csv'
    else:
        result_file = sys.argv[3]

    list_users = []
    with open(user_file, 'r', encoding='utf-8') as f:
        for line in f:
            list_data = line.split(',')
            user_data = ['', '', '']
            for i in range(len(list_data)):
                if i < 3:
                    user_data[i] = list_data[i].strip()
            """Выбран тип словарь, чтобы иметь доступ к каждой отдельной части ФИО"""
            list_users.append({'surname': user_data[0],
                               'name': user_data[1],
                               'patronymic': user_data[2]})

    list_hobby = []
    with open(hobby_file, 'r', encoding='utf-8') as f:
        for line in f:
            """Выбран список, потому что другие типы тут излишние"""
            list_hobby.append(list(map(lambda str: str.strip(), line.split(','))))

    if len(list_hobby) > len(list_users):
        exit(1)

    result_dict = {}
    for i in range(len(list_users)):
        user = list_users[i]
        full_name = ' '.join(user.values())
        result_dict[full_name] = get_elem(i, list_hobby)

    with open(result_file, 'w', encoding='utf-8') as f:
        for key, value in result_dict.items():
            f.write(f'{key}: {value}\n')
