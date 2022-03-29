work_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for element in work_list:
    elem_list = element.split()
    last_index = len(elem_list) - 1
    name = elem_list[last_index].capitalize()
    print(f'Привет, {name}!')
