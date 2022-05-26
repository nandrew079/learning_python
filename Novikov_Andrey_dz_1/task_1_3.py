list_percent = [i for i in range(1, 101)]
for i in list_percent:
    rest = i % 10
    if rest == 0 or 5 <= rest <= 9 or 11 <= i <= 14:
        print(f'{i} процентов')
    elif 2 <= rest <= 4:
        print(f'{i} процента')
    else:
        print(f'{i} процент')
