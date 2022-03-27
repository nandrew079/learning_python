duration = int(input('Введите количество секунд: '))
list_time = []
time_str = ''

while duration != 0:
    if len(list_time) == 0:
        rest = duration % 60
        time_str = f'{rest} сек'
        list_time.append(rest)
        duration = duration // 60
    elif len(list_time) == 1:
        rest = duration % 60
        time_str = f'{rest} мин' + ' ' + time_str
        list_time.append(rest)
        duration = duration // 60
    elif len(list_time) == 2:
        rest = duration % 24
        time_str = f'{rest} час' + ' ' + time_str
        list_time.append(rest)
        duration = duration // 24
    else:
        time_str = f'{duration} дн' + ' ' + time_str
        list_time.append(duration)
        duration = 0

print(time_str)
