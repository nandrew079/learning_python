list_number = [i**3 for i in range(1, 1001)]

list_seven = []
for i in list_number:
    str_number = str(i)
    sum_number = 0
    for j in str_number:
        sum_number = sum_number + int(j)
    if sum_number % 7 == 0:
        list_seven.append(i)

print('a) ', list_seven)

list_seven = []
for i in list_number:
    new_number = i + 17
    str_number = str(new_number)
    sum_number = 0
    for j in str_number:
        sum_number = sum_number + int(j)
    if sum_number % 7 == 0:
        list_seven.append(new_number)

print('c) ', list_seven)
