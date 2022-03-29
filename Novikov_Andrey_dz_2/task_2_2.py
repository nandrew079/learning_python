import re

work_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for element in work_list:
    if element.isdigit() or re.match(r'[-+]?\d+', element):
        str_format = '02'
        sign = str(element[0])
        if sign == '+' and '-':
            str_format = f'{sign}03'

        new_list.append('"')
        new_list.append(f'{int(element):{str_format}}')
        new_list.append('"')
    else:
        new_list.append(element)

final_str = ''
flag = True
for element in new_list:
    if element == '"':
        flag = not flag
    final_str += str(element)
    if flag:
        final_str += ' '

print(final_str)
