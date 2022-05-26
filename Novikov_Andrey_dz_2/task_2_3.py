import re

work_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(work_list))

i = 0
while i < len(work_list):
    element = work_list[i]
    if element.isdigit() or re.match(r'[-+]?\d+', element):
        str_format = '02'
        sign = str(element[0])
        if sign == '+' and '-':
            str_format = f'{sign}03'

        work_list.insert(i, '"')
        i += 1
        work_list[i] = f'{int(element):{str_format}}'
        i += 1
        work_list.insert(i, '"')
        i += 1
    i += 1
print(id(work_list))

final_str = ''
flag = True
for element in work_list:
    if element == '"':
        flag = not flag
    final_str += str(element)
    if flag:
        final_str += ' '

print(final_str)
