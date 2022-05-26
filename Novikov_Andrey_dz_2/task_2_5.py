price_list = [57.8, 46.51, 97, 15, 25.75, 68.3, 2, 18.85, 95, 10]
final_str = ''
for elem in price_list:
    elem_list = str(elem).split('.')
    rub = f'{elem_list[0]:02}'
    kop = '00'
    if len(elem_list) == 2:
        kop = f'{elem_list[1]:02}'
    final_str += f'{rub} руб {kop} коп, '

final_str = final_str[:-2]
print(final_str)

print(id(price_list))
price_list.sort()
print(price_list)
print(id(price_list))

new_list = sorted(price_list, reverse=True)
print(new_list)

print(new_list[:5])
